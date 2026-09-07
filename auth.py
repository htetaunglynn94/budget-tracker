from google.oauth2.credentials import Credentials
import requests
import streamlit as st
from streamlit_oauth import OAuth2Component

# Replace with your actual Formspree endpoint URL
FORMSPREE_ENDPOINT = "https://formspree.io/f/meaqrzjl"


class GoogleAuth:

    def __init__(self):
        self.client_id = st.secrets["client_id"]
        self.client_secret = st.secrets["client_secret"]
        self.redirect_uri = st.secrets["redirect_uri"]

        self.authorize_url = "https://accounts.google.com/o/oauth2/v2/auth"
        self.token_url = "https://oauth2.googleapis.com/token"
        self.scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/userinfo.email",
        ]

        self.oauth2 = OAuth2Component(
            self.client_id,
            self.client_secret,
            self.authorize_url,
            self.token_url,
            self.token_url,
            self.redirect_uri,
        )

    def get_credentials(self):
        if "token" not in st.session_state:
            st.session_state["token"] = None

        if not st.session_state["token"]:
            st.title("🔑 Budget Tracker - Login")
            st.write("Please sign in with your Google account to continue.")

            # -----------------------------------------------------------------
            # 1. Google Sign-In Button
            # -----------------------------------------------------------------
            result = self.oauth2.authorize_button(
                name="Sign in with Google",
                icon="https://www.google.com/favicon.ico",
                redirect_uri=self.redirect_uri,
                scope=" ".join(self.scopes),
                key="google_auth",
            )

            if result and "token" in result:
                st.session_state["token"] = result["token"]
                st.rerun()

            st.divider()

            # -----------------------------------------------------------------
            # 2. Access Request Form for New Testers
            # -----------------------------------------------------------------
            st.subheader("🙋 Need Access?")
            st.caption(
                "This app is currently in testing mode. If you receive an access denied error, submit your email below to request access."
            )

            with st.form("request_access_form", clear_on_submit=True):
                user_email = st.text_input(
                    "Your Google Email Address",
                    placeholder="example@gmail.com",
                )
                submit_req = st.form_submit_button("Request Access")

                if submit_req:
                    if user_email and "@" in user_email:
                        # Send email notification via Formspree API
                        payload = {
                            "email": user_email,
                            "message": f"User {user_email} requested access to the Budget Tracker app.",
                        }
                        try:
                            response = requests.post(
                                FORMSPREE_ENDPOINT, json=payload
                            )
                            if response.status_code == 200:
                                st.success(
                                    "Request submitted! The developer will add your email to the test user list shortly."
                                )
                            else:
                                st.error(
                                    "Failed to send request. Please try again later."
                                )
                        except Exception as e:
                            st.error(f"Error submitting request: {e}")
                    else:
                        st.warning("Please enter a valid email address.")

            return None

        return Credentials(st.session_state["token"]["access_token"])