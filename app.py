import streamlit as st
import asyncio
import websockets
import json

# WebSocket details
WEBSOCKET_URL = (
    "wss://socf-lok-live.leagueofkingdoms.com/socket.io/"
    "?EIO=4&transport=websocket&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzQ1NWIwYzIyZmI0ODRhMDVkYTg3ZWQiLCJraW5nZG9tSWQiOiI2NzQ1NWIwZDIyZmI0ODRhMDVkYTg3ZjQiLCJ3b3JsZElkIjo2MSwidmVyc2lvbiI6MTc4OSwiYXV0aFR5cGUiOiJjYXJ2IiwicGxhdGZvcm0iOiJ3ZWIiLCJ0aW1lIjoxNzM4OTA4ODM3NDkyLCJjbGllbnRYb3IiOiIwIiwiaXAiOiIxNTIuNTkuMjQyLjQyIiwiaWF0IjoxNzM4OTA4ODM3LCJleHAiOjE3Mzk1MTM2MzcsImlzcyI6Im5vZGdhbWVzLmNvbSIsInN1YiI6InVzZXJJbmZvIn0.n0OZAuPnw0NR0RaTxbmp_1hskZwFGDrLUQH5afJorpI"
)

# Async function to connect and send a command
async def connect_and_send(command):
    try:
        async with websockets.connect(WEBSOCKET_URL) as websocket:
            # Initial handshake
            await websocket.send("40")
            ack = await websocket.recv()
            st.write("Acknowledgment Received:", ack)

            # Send command
            await websocket.send(f"42[{json.dumps(command)}]")
            st.write(f"Sent command: {command}")

            # Receive responses
            responses = []
            for _ in range(10):  # Adjust based on expected response count
                response = await websocket.recv()
                responses.append(response)

            return responses
    except Exception as e:
        return [f"WebSocket Error: {str(e)}"]

# Streamlit app
st.title("Streamlit WebSocket Scanner")

# Command selection
st.subheader("Available Functions")
available_functions = {
    "Scan Kingdoms": ["scan"],
    "Get Player Details": ["get_player_details"],
    "Fetch Resources": ["fetch_resources"],
}

command = st.selectbox("Choose a function to execute:", list(available_functions.keys()))

if st.button("Execute Command"):
    st.write(f"Executing command: {command}...")
    selected_command = available_functions[command]
    responses = asyncio.run(connect_and_send(selected_command))
    st.write("Responses:")
    for msg in responses:
        st.json(msg)
