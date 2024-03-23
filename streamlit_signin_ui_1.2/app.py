import pandas as pd
import streamlit as st
from streamlit_signin_auth_ui.widgets import __login__

secrets_auth = st.secrets["google_sheets_api_credentials"]
secrets_auth = secrets_auth
smtp_gmail_ = st.secrets.smtp_gmail
smtp_password_ = st.secrets.smtp_password


__login__obj = __login__(credentials=secrets_auth,
                    smtp_username = smtp_gmail_,
                    smtp_password = smtp_password_,
                    company_name = "Tesla",
                    width = 200, height = 300,
                    logout_button_name = 'Sortir', hide_menu_bool = False,
                    hide_footer_bool = False,
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')



LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:
    st.success("Bienvenue!")
