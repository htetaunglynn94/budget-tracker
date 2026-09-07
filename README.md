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

## ⚙️ Detailed Setup & Configuration Guide

Follow these steps to set up the Google Cloud Platform (GCP) credentials, enable the necessary Google APIs, and configure your secrets for deployment.

---

### Step 1: Google Cloud Console Setup

1. **Create a New GCP Project:**
   * Go to the [Google Cloud Console](https://console.cloud.google.com/).
   * Click the project dropdown in the top bar and select **New Project**.
   * Name your project (e.g., `Budget Tracker`) and click **Create**.

2. **Enable Required APIs:**
   * In the left sidebar, navigate to **APIs & Services** > **Library**.
   * Search for **Google Drive API** and click **Enable**.
   * Search for **Google Sheets API** and click **Enable**.

3. **Configure the OAuth Consent Screen:**
   * Go to **APIs & Services** > **OAuth consent screen** (or **Audience** in the Google Auth Platform menu).
   * Select **External** as the user type and click **Create**.
   * Fill in the basic app details (App name, User support email, Developer contact email).
   * Save and continue through the **Scopes** step.
   * Under **Test users**, click **+ ADD USERS** and enter your Google email address (and any tester emails).
   * *(Optional)* Click **Publish App** if you want to bypass the 100 test user limit and allow any Google account to sign in.

4. **Create OAuth 2.0 Credentials:**
   * Go to **APIs & Services** > **Credentials**.
   * Click **+ CREATE CREDENTIALS** at the top and select **OAuth client ID**.
   * Choose **Web application** as the Application type.
   * Under **Authorized redirect URIs**, add your local and live application URLs:
     * `http://localhost:8501` *(for local testing)*
     * `https://YOUR-APP-NAME.streamlit.app` *(for live deployment)*
   * Click **Create**.
   * Copy the generated **Client ID** and **Client Secret**.

---

### Step 2: Google Drive & Sheets Integration

You do **not** need to manually create a Google Sheet! 

* The application uses the logged-in user's OAuth credentials via `gspread`.
* Upon first sign-in, the app automatically checks the user's personal Google Drive for a file named `Daily Budget`.
* If missing, the app creates the spreadsheet and a `Transactions` worksheet pre-configured with the following header schema:
  `["Date", "Type", "Category", "Sub-category", "Payment Method", "Decision", "Amount", "Description"]`

---

### Step 3: Streamlit Configuration & Secrets

#### Local Environment Configuration
Create a file at `.streamlit/secrets.toml` in your project root directory and add your credentials:

```toml
client_id = "YOUR_CLIENT_ID.apps.googleusercontent.com"
client_secret = "YOUR_CLIENT_SECRET"
redirect_uri = "http://localhost:8501"
```

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
