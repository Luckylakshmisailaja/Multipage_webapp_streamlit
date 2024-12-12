import streamlit as st

# ----   PAGE SETUP  ----
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)

project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

# # ---- Navigation setup[without sections] -----
# pg = st.navigation(pages=[about_page,project_1_page,project_2_page])

# ---- Navigation setup[with sections] -----
pg = st.navigation(
    {
        "Info": [about_page],
        'Projects': [project_1_page,project_2_page],
    }
)

# --- Shared on all pages ----
st.logo("assets/codingisfun_logo.png")
st.sidebar.text("Made with 🩷 by Lakshmi")
# st.logo("assets/Profile_Image.jpg")
# --- Run Navigation ----
pg.run()