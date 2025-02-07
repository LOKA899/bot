import streamlit as st
import requests

# API Details
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzQ1NWIwYzIyZmI0ODRhMDVkYTg3ZWQiLCJraW5nZG9tSWQiOiI2NzQ1NWIwZDIyZmI0ODRhMDVkYTg3ZjQiLCJ3b3JsZElkIjo2MSwidmVyc2lvbiI6MTc4OSwiYXV0aFR5cGUiOiJjYXJ2IiwicGxhdGZvcm0iOiJ3ZWIiLCJ0aW1lIjoxNzM4OTA4ODM3NDkyLCJjbGllbnRYb3IiOiIwIiwiaXAiOiIxNTIuNTkuMjQyLjQyIiwiaWF0IjoxNzM4OTA4ODM3LCJleHAiOjE3Mzk1MTM2MzcsImlzcyI6Im5vZGdhbWVzLmNvbSIsInN1YiI6InVzZXJJbmZvIn0.n0OZAuPnw0NR0RaTxbmp_1hskZwFGDrLUQH5afJorpI"
API_URL = "https://api-lok-live.leagueofkingdoms.com/api"

# Fetch Kingdom Name
def fetch_kingdom_data():
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    try:
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("account", {}).get("kingdom", {}).get("name", "Unknown Kingdom")
        else:
            st.error(f"Error: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Request failed: {e}")
        return None

# Streamlit App
st.title("Kingdom Name Fetcher")

if st.button("Fetch Kingdom Name"):
    kingdom_name = fetch_kingdom_data()
    if kingdom_name:
        st.success(f"Kingdom Name: {kingdom_name}")
    else:
        st.error("Failed to fetch kingdom name.")
