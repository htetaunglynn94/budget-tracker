# 💰 Daily Budget Tracker

A multi-user daily budget and expense tracking web application built with **Python**, **Streamlit**, **Plotly**, and **Google Sheets API**. 

The application allows users to securely sign in using their own Google account. Once authenticated, the app automatically creates and manages a dedicated `Daily Budget` spreadsheet inside the user's personal Google Drive to store, track, and visualize financial records.

🔗 **Live Application:** [Daily Budget Tracker WebApp](https://budget-tracker-imtvdsmv3oinshxqtobhvj.streamlit.app/)

---

## 🌟 Key Features

* **Multi-User Google Authentication**: Secure login allowing each user to connect their personal Google Drive without exposing database credentials.
* **Automated Sheet Setup**: Automatically checks for and creates the `Daily Budget` spreadsheet and `Transactions` worksheet with proper schema on first login.
* **Daily Expense Logging**: Form to capture transaction details including Date, Type, Category, Sub-category, Payment Method, Decision (Need vs. Want), Amount, and Description.
* **Expense History & Summaries**: Clean tabular view of logged transactions with formatted date styling (`dd-MMM-yyyy`) and aggregate metric cards (Total Income vs. Total Expenses).
* **Interactive Analytics Dashboard**:
  * **Type Distribution**: Overview of all recorded financial flows.
  * **Category Breakdown**: Expense distribution by category.
  * **Needs vs. Wants Ratio**: Decision analysis to monitor discretionary spending.
  * **Daily Spending Trend**: Time-series bar chart highlighting daily expenditure.
* **🙋 In-App Access Request**: Built-in access request form for new test users during developer testing phases.

---

## 📁 Project Architecture

The project follows a clean, Object-Oriented Programming (OOP) modular design:

```text
budget-tracker/
├── .streamlit/
│   └── secrets.toml         # Encrypted local secrets configuration
├── app.py                   # Main Streamlit application entry point
├── auth.py                  # Google OAuth 2.0 authentication handler
├── sheet_manager.py         # Google Sheets CRUD & auto-provisioning class
├── visualization.py         # Plotly chart generation class
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## 🔮 Future Developments
Planned features and roadmap for future versions of the application:

- **Direct Record Editing & Deletion**: Interactive table editing (using st.data_editor) allowing users to update or delete past transactions directly from the web interface without opening Google Sheets.
- **Custom Categories & Transaction Types**: Options for users to dynamically add, edit, or remove custom Type and Category dropdown values to fit personal budgeting preferences.

- **Advanced Custom Charts & Analytics**:
    - Monthly budget target tracker with threshold alerts
    - Payment method breakdown (Cash vs. Card vs. E-Wallet spending ratio).
    - Date range and monthly filtering controls across all dashboard charts.

- **Data Export Options**: Direct PDF and CSV export buttons for generating monthly spending summary reports.


---

## Contact

If you have feedback or opportunities, feel free to connect:

* [LinkedIn](www.linkedin.com/in/htetaglynn)
* [GitHub](https://github.com/htetaunglynn94)
---
