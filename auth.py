from google.oauth2.credentials import Credentials
import streamlit as st
from streamlit_oauth import OAuth2Component


class GoogleAuth:

    def __init__(self):
        self.client_id = st.secrets["client_id"]
        self.client_secret = st.secrets["client_secret"]
        self.redirect_uri = st.secrets["redirect_uri"]

        self.authorize_url = "https://accounts.google.com/o/oauth2/v2/auth"
        self.token_url = "https://oauth2.googleapis.com/token"
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets",
                       "https://www.googleapis.com/auth/drive",
                       "https://www.googleapis.com/auth/userinfo.email"]

        self.oauth2 = OAuth2Component(self.client_id,
                                      self.client_secret,
                                      self.authorize_url,
                                      self.token_url,
                                      self.token_url,
                                      self.redirect_uri)

    def get_credentials(self):
        if "token" not in st.session_state:
            st.session_state["token"] = None

        if not st.session_state["token"]:
            st.title("🔑 Budget Tracker - Login")
            st.write("Please sign in with your Google account to continue.")

            result = self.oauth2.authorize_button(name = "Sign in with Google",
                                                  icon = "https://www.google.com/favicon.ico",
                                                  redirect_uri = self.redirect_uri,
                                                  scope = " ".join(self.scopes),
                                                  key = "google_auth")

            if result and "token" in result:
                st.session_state["token"] = result["token"]
                st.rerun()

            return None

        return Credentials(st.session_state["token"]["access_token"])