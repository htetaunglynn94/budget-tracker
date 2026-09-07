import datetime
import gspread
from auth import GoogleAuth
from sheet_manager import SheetManager
import streamlit as st
from visualization import BudgetVisualizer

st.set_page_config(
    page_title="Daily Budget Tracker", page_icon="💰", layout="wide"
)

# 1. Handle Authentication
auth_handler = GoogleAuth()
user_creds = auth_handler.get_credentials()

if user_creds:
    # Sidebar logout
    if st.sidebar.button("Logout"):
        st.session_state["token"] = None
        st.rerun()

    # 2. Initialize Sheet Manager
    client = gspread.authorize(user_creds)
    sheet_mgr = SheetManager(client)

    st.title("💰 Daily Budget Tracker")
    menu = st.sidebar.radio(
        "MENU", ["Add Transaction", "View Records", "Visualize Data"]
    )

    # -------------------------------------------------------------------------
    # TAB 1: ADD TRANSACTION
    # -------------------------------------------------------------------------
    if menu == "Add Transaction":
        st.subheader("Log New Transaction")
        with st.form("entry_form", clear_on_submit=True):
            col1, col2, col3 = st.columns(3)
            date = col1.date_input("Date", datetime.date.today())
            trans_type = col2.selectbox(
                "Type", ["Expense", "Income", "Over Time", "Saving", "Other"]
            )
            decision = col3.selectbox("Decision", ["Need", "Want"])

            col4, col5 = st.columns(2)
            category = col4.selectbox(
                "Category",
                [
                    "Food",
                    "Transportation",
                    "Cosmetic",
                    "Bills",
                    "Shopping",
                    "Income",
                    "Over Time",
                    "Saving",
                    "Other",
                ],
            )
            sub_category = col5.text_input(
                "Sub-category (e.g., Groceries, OT)"
            )

            col6, col7 = st.columns(2)
            payment_method = col6.selectbox(
                "Payment Method",
                ["Banking", "Cash", "E-Wallet", "Credit Card"],
            )
            amount = col7.number_input(
                "Amount ($)", min_value=0.0, format="%.2f"
            )

            description = st.text_input("Description")
            submitted = st.form_submit_button("Save Record")

            if submitted:
                new_row = [
                    str(date),
                    trans_type,
                    category,
                    sub_category,
                    payment_method,
                    decision,
                    amount,
                    description,
                ]
                sheet_mgr.add_transaction(new_row)
                st.success("Transaction saved successfully!")

    # -------------------------------------------------------------------------
    # TAB 2: VIEW RECORDS
    # -------------------------------------------------------------------------
    elif menu == "View Records":
        st.subheader("Expense History")
        df = sheet_mgr.get_data_as_df()

        if not df.empty:
            st.dataframe(df, use_container_width=True)
            st.divider()

            total_income = df[df["Type"].isin(["Income", "Over Time"])][
                "Amount"
            ].sum()
            total_expense = df[df["Type"] == "Expense"]["Amount"].sum()

            m1, m2 = st.columns(2)
            m1.metric("Total Income (Inc. OT)", f"${total_income:,.2f}")
            m2.metric("Total Expenses", f"${total_expense:,.2f}")
        else:
            st.info("No records found.")

    # -------------------------------------------------------------------------
    # TAB 3: VISUALIZE DATA
    # -------------------------------------------------------------------------
    elif menu == "Visualize Data":
        st.subheader("📊 Expense Statistics")
        df = sheet_mgr.get_data_as_df()

        if not df.empty:
            visualizer = BudgetVisualizer(df)

            st.markdown("### Distribution")
            c1, c2, c3 = st.columns(3)

            with c1:
                st.plotly_chart(
                    visualizer.plot_type_pie(), use_container_width=True
                )

            with c2:
                cat_chart = visualizer.plot_category_pie()
                if cat_chart:
                    st.plotly_chart(cat_chart, use_container_width=True)
                else:
                    st.info("No expense categories available.")

            with c3:
                dec_chart = visualizer.plot_decision_pie()
                if dec_chart:
                    st.plotly_chart(dec_chart, use_container_width=True)
                else:
                    st.info("No expense decisions available.")

            st.divider()

            st.markdown("### Daily Expense Overview")
            daily_chart = visualizer.plot_daily_trend()
            if daily_chart:
                st.plotly_chart(daily_chart, use_container_width=True)
            else:
                st.info("No expense records available for daily trend.")
        else:
            st.info("No records found to visualize.")

    # -------------------------------------------------------------------------
    # FOOTER / INTELLECTUAL PROPERTY NOTICE
    # -------------------------------------------------------------------------
    st.sidebar.markdown("---")
    st.sidebar.caption("© 2026 Daily Budget Tracker")
    st.sidebar.markdown("**This application was created by Htet Aung Lynn**")