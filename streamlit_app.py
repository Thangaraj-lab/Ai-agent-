# ui/streamlit_app.py

import streamlit as st
import requests
import json

from utils.logger import get_logger


logger = get_logger(__name__)


API_URL = "http://127.0.0.1:8000/ask"


# -------------------------------
# 🔹 APP CONFIG
# -------------------------------
st.set_page_config(
    page_title="Agent AI Dashboard",
    layout="wide"
)

st.title("🚀 Agent AI Decision Dashboard")


# -------------------------------
# 🔹 INPUT SECTION
# -------------------------------
st.sidebar.header("Input Data")

num_users = st.sidebar.number_input("Number of Users", min_value=1, max_value=20, value=3)

users = []

for i in range(num_users):
    user_id = st.sidebar.text_input(f"User ID {i+1}", f"U{i+1}")
    revenue = st.sidebar.number_input(f"Revenue {i+1}", min_value=0.0, value=1000.0)

    users.append({
        "user_id": user_id,
        "expected_revenue": revenue
    })


query = st.text_input("Ask AI (e.g., 'Who is best?')")


# -------------------------------
# 🔹 ANALYZE BUTTON
# -------------------------------
if st.button("Analyze"):
    try:
        payload = {
            "query": query,
            "data": {
                "all_users": users,
                "top_users": users
            }
        }

        response = requests.post(API_URL, params={"query": query}, json=payload)

        if response.status_code == 200:
            result = response.json()

            st.success("Analysis Completed")

            # 🔹 Show AI response
            st.subheader("🤖 AI Response")
            st.write(result.get("response"))

            # 🔹 Show intent
            st.subheader("🎯 Detected Intent")
            st.write(result.get("intent"))

            # 🔹 Show history
            st.subheader("🧠 Memory (Last Queries)")
            st.write(result.get("history"))

        else:
            st.error("API Error")

    except Exception as e:
        logger.error(f"UI error: {str(e)}")
        st.error("Something went wrong")