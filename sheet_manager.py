import gspread
import pandas as pd


class SheetManager:

    def __init__(
        self, client: gspread.Client, sheet_name: str = "Daily Budget"):
        self.client = client
        self.sheet_name = sheet_name
        self.headers = ["Date",
                        "Type",
                        "Category",
                        "Sub-category",
                        "Payment Method",
                        "Decision",
                        "Amount",
                        "Description"]
        
        self.worksheet = self._get_or_create_sheet()

    def _get_or_create_sheet(self) -> gspread.Worksheet:
        """Finds or creates the budget spreadsheet and 'Transactions' tab."""
        try:
            spreadsheet = self.client.open(self.sheet_name)
        except gspread.exceptions.SpreadsheetNotFound:
            spreadsheet = self.client.create(self.sheet_name)
            worksheet = spreadsheet.sheet1
            worksheet.update_title("Transactions")
            worksheet.append_row(self.headers)
            return worksheet

        try:
            return spreadsheet.worksheet("Transactions")
        except gspread.exceptions.WorksheetNotFound:
            worksheet = spreadsheet.add_worksheet(
                title="Transactions", rows=100, cols=10
            )
            worksheet.append_row(self.headers)
            return worksheet

    def add_transaction(self, record_data: list):
        """Appends a single transaction row to the Google Sheet."""
        self.worksheet.append_row(record_data)

    def get_data_as_df(self) -> pd.DataFrame:
        """Fetches all records from Google Sheet and returns a cleaned pandas DataFrame."""
        records = self.worksheet.get_all_records()
        if not records:
            return pd.DataFrame(columns=self.headers)

        df = pd.DataFrame(records)
        if "Amount" in df.columns:
            df["Amount"] = pd.to_numeric(
                df["Amount"].astype(str).str.replace("$", ""), errors="coerce"
            ).fillna(0.0)

        if "Date" in df.columns:
            # Convert to datetime and reformat as dd-MMM-yyyy
            df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
            df["Date"] = df["Date"].dt.strftime("%d-%b-%Y")

        return df