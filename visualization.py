import pandas as pd
import plotly.express as px


class BudgetVisualizer:

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.expenses_df = (
            df[df["Type"] == "Expense"] if not df.empty else pd.DataFrame()
        )

    def _apply_bottom_legend(self, fig):
        """Helper method to place pie chart legends neatly at the bottom."""
        fig.update_traces(
            textinfo="percent", hoverinfo="label+value+percent"
        )
        fig.update_layout(
            legend=dict(
                orientation="h", yanchor="top", y=-0.1, xanchor="center", x=0.5
            ),
            margin=dict(l=10, r=10, t=40, b=50),
        )
        return fig

    def plot_type_pie(self):
        """Pie chart for all transaction types."""
        type_df = self.df.groupby("Type")["Amount"].sum().reset_index()
        fig = px.pie(type_df,
                     names = "Type",
                     values = "Amount",
                     title = "All Expense vs. Income",
                     hole = 0.4)
        
        return self._apply_bottom_legend(fig)

    def plot_category_pie(self):
        """Pie chart for expense categories."""
        if self.expenses_df.empty:
            return None
        cat_df = (
            self.expenses_df.groupby("Category")["Amount"].sum().reset_index()
        )
        fig = px.pie(cat_df,
                     names = "Category",
                     values = "Amount",
                     title = "Expense by Category",
                     hole = 0.4)
        return self._apply_bottom_legend(fig)

    def plot_decision_pie(self):
        """Pie chart for Needs vs Wants."""
        if self.expenses_df.empty:
            return None
        
        decision_df = (self.expenses_df.groupby("Decision")["Amount"].sum().reset_index())

        fig = px.pie(decision_df,
                     names = "Decision",
                     values = "Amount",
                     title = "Need vs Want",
                     color = "Decision",
                     color_discrete_map = {"Need": "#2E7D32", "Want": "#D32F2F"},
                     hole = 0.4)
        return self._apply_bottom_legend(fig)

    def plot_daily_trend(self):
        """Bar chart for daily expenses."""
        if self.expenses_df.empty:
            return None
        daily_spending = (self.expenses_df.groupby("Date")["Amount"].sum().reset_index())

        fig = px.bar(daily_spending,
                     x = "Date",
                     y = "Amount",
                     title = "Daily Expense Trend",
                     labels = {"Amount": "Total Spent ($)", "Date": "Date"},
                     text_auto = ".2f")
        
        fig.update_traces(marker_color="#1E88E5")
        return fig