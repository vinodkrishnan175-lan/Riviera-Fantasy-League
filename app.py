import streamlit as st
import pandas as pd
import psycopg2
import socket



# -------------------
# DB CONNECTION TEST
# -------------------
import socket

def get_ipv4_host(hostname: str) -> str:
    infos = socket.getaddrinfo(hostname, None, family=socket.AF_INET)
    return infos[0][4][0]

def db_healthcheck():
    try:
        host = st.secrets["db"]["host"]
        host_ipv4 = get_ipv4_host(host)
        conn = psycopg2.connect(
            host=host_ipv4,
            port=st.secrets["db"]["port"],
            dbname=st.secrets["db"]["dbname"],
            user=st.secrets["db"]["user"],
            password=st.secrets["db"]["password"],
            sslmode="require",
            connect_timeout=5,
        )
        conn.close()
        return True, "DB Connected"
    except Exception as e:
        return False, f"DB Error: {type(e).__name__}: {e}"

ok, msg = db_healthcheck()
if ok:
    st.success(msg)
else:
    st.error(f"{msg} (host={st.secrets['db']['host']})")
    st.stop()
# -------------------
# PAGE CONFIG
# -------------------
left, right = st.columns([5, 2])
with right:
    if ok:
        st.success(msg)
    else:
        st.error(msg)
        st.stop()
st.set_page_config(
    page_title="Riviera Fantasy League",
    page_icon="🏆",
    layout="wide"
)
def get_ipv4_host(hostname: str) -> str:
    infos = socket.getaddrinfo(hostname, None, family=socket.AF_INET)
    return infos[0][4][0]

def db_healthcheck():
    try:
        host = st.secrets["db"]["host"]
        host_ipv4 = get_ipv4_host(host)
        conn = psycopg2.connect(
            host=host_ipv4,
            port=st.secrets["db"]["port"],
            dbname=st.secrets["db"]["dbname"],
            user=st.secrets["db"]["user"],
            password=st.secrets["db"]["password"],
            sslmode="require",
            connect_timeout=5,
        )
        conn.close()
        return True, "DB Connected"
    except Exception as e:
        return False, f"DB Error: {type(e).__name__}"

ok, msg = db_healthcheck()
badge_color = "#00C48C" if ok else "#FF4D4F"

st.markdown(
    f"""
    <div style="
        position: fixed;
        top: 18px;
        right: 18px;
        z-index: 9999;
        background: #1A1F2E;
        border: 1px solid {badge_color};
        color: #EAEAEA;
        padding: 8px 12px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 12px;
        ">
        <span style="color:{badge_color};">●</span> {msg}
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------
# PREMIUM DARK THEME
# -------------------
st.markdown("""
<style>
body {
    background-color: #0B0F18;
}
[data-testid="stAppViewContainer"] {
    background-color: #0B0F18;
}
h1, h2, h3, h4, h5, h6, p, span, label {
    color: #EAEAEA !important;
}
.stButton>button {
    background: linear-gradient(90deg, #D4AF37, #F5C542);
    color: black;
    font-weight: bold;
    border-radius: 10px;
}
.card {
    background-color: #1A1F2E;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
}
.gold {
    color: #F5C542;
}
</style>
""", unsafe_allow_html=True)

# -------------------
# HEADER
# -------------------
st.markdown("<h1 class='gold'>RIVIERA FANTASY LEAGUE</h1>", unsafe_allow_html=True)
st.markdown("<h4>Premium Weekend Fantasy Experience</h4>", unsafe_allow_html=True)

# -------------------
# NAVIGATION
# -------------------
menu = st.selectbox(
    "",
    ["Home", "Pick Team", "My Teams", "Match Leaderboard", "Season Leaderboard", "Player Stats", "Admin"]
)

st.markdown("---")

# -------------------
# SAMPLE PAGES
# -------------------

if menu == "Home":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Select Active Match")
    st.write("Match selector will appear here.")
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Pick Team":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Build Your Dream XI")
    st.write("Team selection grid will go here.")
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Match Leaderboard":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Match Leaderboard")
    st.write("Leaderboard table here.")
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Season Leaderboard":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Season Standings")
    st.write("Cumulative leaderboard.")
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Player Stats":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Top Fantasy Players")
    st.write("Batting / Bowling / Fielding charts.")
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Admin":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Admin Panel")
    st.write("Create matches, assign squads, enter stats.")
    st.markdown("</div>", unsafe_allow_html=True)
