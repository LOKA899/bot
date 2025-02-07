import streamlit as st
import asyncio
import websockets

async def connect_to_websocket():
    url = "wss://sock-lok-live.leagueofkingdoms.com/socket.io/"
    try:
        async with websockets.connect(url) as websocket:
            # Example: Send a message if needed
            # await websocket.send("Your Message Here")
            response = await websocket.recv()
            return response
    except Exception as e:
        return str(e)

st.title("WebSocket Data Viewer")
if st.button("Fetch WebSocket Data"):
    data = asyncio.run(connect_to_websocket())
    st.write("Data Received:", data)
