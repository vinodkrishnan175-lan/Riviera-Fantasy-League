import streamlit as st
import pandas as pd
import psycopg2
import socket

# -------------------
# DB CONNECTION TEST
# -------------------
def get_ipv4_host(hostname: str) -> str:
    # Resolve hostname to IPv4 to avoid IPv6 connectivity issues on Streamlit Cloud
    infos = socket.getaddrinfo(hostname, None, family=socket.AF_INET)
    # infos[0][4][0] is the IPv4 string
    return infos[0][4][0]

def test_connection():
    try:
        host = st.secrets["db"]["host"]
        host_ipv4 = get_ipv4_host(host)

        conn = psycopg2.connect(
            host=host_ipv4,  # use IPv4 address
            port=st.secrets["db"]["port"],
            dbname=st.secrets["db"]["dbname"],
            user=st.secrets["db"]["user"],
            password=st.secrets["db"]["password"],
            sslmode="require"
        )
        conn.close()
        return True
    except Exception as e:
        return str(e)
# -------------------
# PAGE CONFIG
# -------------------
st.set_page_config(
    page_title="Riviera Fantasy League",
    page_icon="🏆",
    layout="wide"
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
