import asyncio
import websockets

# WebSocket URL
WEBSOCKET_URL = "wss://socf-lok-live.leagueofkingdoms.com/socket.io/?EIO=4&transport=websocket&token=YOUR_ACCESS_TOKEN"

async def scan_data():
    try:
        async with websockets.connect(WEBSOCKET_URL) as websocket:
            # Initial handshake
            await websocket.send("40")  # Socket.IO connection start
            ack = await websocket.recv()
            print("Acknowledgment Received:", ack)

            # Send scan command (adjust based on protocol)
            await websocket.send("42[\"scan\"]")

            # Receive responses
            responses = []
            for _ in range(5):  # Adjust number of responses
                response = await websocket.recv()
                responses.append(response)

            print("Scan Data Received:")
            for msg in responses:
                print(msg)

    except Exception as e:
        print("Error:", e)

# Run the WebSocket scanning function
asyncio.run(scan_data())
