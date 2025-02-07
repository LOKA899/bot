import streamlit as st
import requests
import asyncio
import websockets

# Data from the uploaded JSON
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzQ1NWIwYzIyZmI0ODRhMDVkYTg3ZWQiLCJraW5nZG9tSWQiOiI2NzQ1NWIwZDIyZmI0ODRhMDVkYTg3ZjQiLCJ3b3JsZElkIjo2MSwidmVyc2lvbiI6MTc4OSwiYXV0aFR5cGUiOiJjYXJ2IiwicGxhdGZvcm0iOiJ3ZWIiLCJ0aW1lIjoxNzM4OTA4ODM3NDkyLCJjbGllbnRYb3IiOiIwIiwiaXAiOiIxNTIuNTkuMjQyLjQyIiwiaWF0IjoxNzM4OTA4ODM3LCJleHAiOjE3Mzk1MTM2MzcsImlzcyI6Im5vZGdhbWVzLmNvbSIsInN1YiI6InVzZXJJbmZvIn0.n0OZAuPnw0NR0RaTxbmp_1hskZwFGDrLUQH5afJorpI"
API_URL = "https://api-lok-live.leagueofkingdoms.com/api"
WEBSOCKET_URL = "wss://sock-lok-live.leagueofkingdoms.com/socket.io/"

# Display Kingdom Data
def display_kingdom():
    st.title("Kingdom Information")
    st.write("**Kingdom Name:** Mysore")
    st.write("**Level:** 21")
    st.write("**Power:** 5,336,780")
    st.write("**Crystals:** 806")

# API Testing
def test_api():
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    try:
        response = requests.get(API_URL, headers=headers)
        st.write("API Response Code:", response.status_code)
        st.json(response.json())
    except Exception as e:
        st.write(f"Error: {e}")

# WebSocket Testing
async def test_websocket():
    try:
        async with websockets.connect(WEBSOCKET_URL) as websocket:
            await websocket.send("42")  # Sending a test message
            response = await websocket.recv()
            st.write("WebSocket Response:", response)
    except Exception as e:
        st.write(f"WebSocket Error: {e}")

# Streamlit Interface
st.sidebar.title("Lokbot Functionality")
option = st.sidebar.selectbox("Select Action", ["Display Kingdom", "Test API", "Test WebSocket"])

if option == "Display Kingdom":
    display_kingdom()
elif option == "Test API":
    test_api()
elif option == "Test WebSocket":
    asyncio.run(test_websocket())
