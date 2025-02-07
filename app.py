import streamlit as st
import asyncio
import websockets

# WebSocket URL and token
WEBSOCKET_URL = "wss://socf-lok-live.leagueofkingdoms.com/socket.io/?EIO=4&transport=websocket&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzQ1NWIwYzIyZmI0ODRhMDVkYTg3ZWQiLCJraW5nZG9tSWQiOiI2NzQ1NWIwZDIyZmI0ODRhMDVkYTg3ZjQiLCJ3b3JsZElkIjo2MSwidmVyc2lvbiI6MTc4OSwiYXV0aFR5cGUiOiJjYXJ2IiwicGxhdGZvcm0iOiJ3ZWIiLCJ0aW1lIjoxNzM4OTA4ODM3NDkyLCJjbGllbnRYb3IiOiIwIiwiaXAiOiIxNTIuNTkuMjQyLjQyIiwiaWF0IjoxNzM4OTA4ODM3LCJleHAiOjE3Mzk1MTM2MzcsImlzcyI6Im5vZGdhbWVzLmNvbSIsInN1YiI6InVzZXJJbmZvIn0.n0OZAuPnw0NR0RaTxbmp_1hskZwFGDrLUQH5afJorpI"

async def connect_to_websocket():
    try:
        async with websockets.connect(WEBSOCKET_URL) as websocket:
            st.success("Connected to WebSocket!")
            
            # Example: Send a test message
            await websocket.send("42")  # Modify this as per protocol requirements
            st.info("Message sent to WebSocket!")

            # Wait for a response
            response = await websocket.recv()
            st.write("Response from WebSocket:", response)
    except Exception as e:
        st.error(f"WebSocket Error: {e}")

# Streamlit app interface
st.title("WebSocket Tester")

if st.button("Connect to WebSocket"):
    st.write("Connecting to WebSocket...")
    asyncio.run(connect_to_websocket())
