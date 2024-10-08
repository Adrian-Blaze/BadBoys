import streamlit as st


# --- PAGE SETUP ---
analysis_page = st.Page(
    "views/productivity_app.py",
    title="Analysis",
    icon=":material/account_circle:",
    default = True
)
study_time_tracker_page = st.Page(
    "views/productivity_app2.py",
    title="Study Time Tracker",
    icon=":material/bar_chart:",
)
leaderboard_page = st.Page(
    "views/productivity_app3.py",
    title="Leaderboard",
    icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Insights": [analysis_page],
        "Productivity": [study_time_tracker_page, leaderboard_page]
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/BBHS.jpg")
st.sidebar.markdown("Made by TEAM BADBOYS")


# --- RUN NAVIGATION ---
pg.run()