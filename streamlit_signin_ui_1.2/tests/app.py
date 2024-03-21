import streamlit as st
from streamlit_signin_auth_ui.widgets import __login__


credentials = {
  "type": "service_account",
  "project_id": "valued-crow-******",
  "private_key_id": "************************************************",
  "private_key": "-----BEGIN PRIVATE KEY-----\*******************************************....*********************=\n-----END PRIVATE KEY-----\n",
  "client_email": "your_project_name@valued-crow-********.iam.gserviceaccount.com",
  "client_id": "************************",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your_project_name%40valued-crow-********.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

__login__obj = __login__(credentials=credentials,
                    smtp_username = 'your_smtp_email',
                    smtp_password = 'your smtp pass word',
                    company_name = "your company name",
                    width = 400, height = 500,
                    logout_button_name = 'Sortir', hide_menu_bool = False,
                    hide_footer_bool = False,
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')



LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:
    st.success("Bienvenue!")
