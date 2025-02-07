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
                try:
                    # Attempt to parse response as JSON
                    parsed_response = json.loads(response)
                    responses.append(parsed_response)
                except json.JSONDecodeError:
                    # Handle non-JSON response
                    responses.append({"raw_response": response})

            return responses
    except Exception as e:
        return [f"WebSocket Error: {str(e)}"]

# Streamlit app
st.title("LOK-Scanner Replication")

# Command selection
st.subheader("Available Commands")
available_commands = {
    "Scan Kingdoms": ["scan"],
    "Fetch Resources": ["fetch_resources"],
    "Get Player Details": ["get_player_details"],
}

selected_command = st.selectbox("Choose a command to execute:", list(available_commands.keys()))

if st.button("Execute Command"):
    st.write(f"Executing command: {selected_command}...")
    command_to_execute = available_commands[selected_command]
    responses = asyncio.run(connect_and_send(command_to_execute))
    st.write("Responses:")
    for msg in responses:
        st.json(msg)
