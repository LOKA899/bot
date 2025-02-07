import requests
import asyncio
import websockets
import json

# API and WebSocket details
API_URL = "https://api-lok-live.leagueofkingdoms.com/api"
WEBSOCKET_URL = "wss://socf-lok-live.leagueofkingdoms.com/socket.io/?EIO=4&transport=websocket&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzQ1NWIwYzIyZmI0ODRhMDVkYTg3ZWQiLCJraW5nZG9tSWQiOiI2NzQ1NWIwZDIyZmI0ODRhMDVkYTg3ZjQiLCJ3b3JsZElkIjo2MSwidmVyc2lvbiI6MTc4OSwiYXV0aFR5cGUiOiJjYXJ2IiwicGxhdGZvcm0iOiJ3ZWIiLCJ0aW1lIjoxNzM4OTA4ODM3NDkyLCJjbGllbnRYb3IiOiIwIiwiaXAiOiIxNTIuNTkuMjQyLjQyIiwiaWF0IjoxNzM4OTA4ODM3LCJleHAiOjE3Mzk1MTM2MzcsImlzcyI6Im5vZGdhbWVzLmNvbSIsInN1YiI6InVzZXJJbmZvIn0.n0OZAuPnw0NR0RaTxbmp_1hskZwFGDrLUQH5afJorpI"
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzQ1NWIwYzIyZmI0ODRhMDVkYTg3ZWQiLCJraW5nZG9tSWQiOiI2NzQ1NWIwZDIyZmI0ODRhMDVkYTg3ZjQiLCJ3b3JsZElkIjo2MSwidmVyc2lvbiI6MTc4OSwiYXV0aFR5cGUiOiJjYXJ2IiwicGxhdGZvcm0iOiJ3ZWIiLCJ0aW1lIjoxNzM4OTA4ODM3NDkyLCJjbGllbnRYb3IiOiIwIiwiaXAiOiIxNTIuNTkuMjQyLjQyIiwiaWF0IjoxNzM4OTA4ODM3LCJleHAiOjE3Mzk1MTM2MzcsImlzcyI6Im5vZGdhbWVzLmNvbSIsInN1YiI6InVzZXJJbmZvIn0.n0OZAuPnw0NR0RaTxbmp_1hskZwFGDrLUQH5afJorpI"

# Fetch data from the API
def fetch_api_data():
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    try:
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"API Error: {response.status_code}", "details": response.text}
    except Exception as e:
        return {"error": str(e)}

# Fetch data from the WebSocket
async def fetch_websocket_data():
    try:
        async with websockets.connect(WEBSOCKET_URL) as websocket:
            await websocket.send("40")  # Initial handshake message for Socket.IO

            # Wait for connection acknowledgment
            ack = await websocket.recv()
            print("Acknowledgment Received:", ack)

            # Sending a test message to fetch data (modify based on protocol specifics)
            await websocket.send("42[\"get_data\"]")

            responses = []
            for _ in range(5):  # Adjust to receive more responses
                response = await websocket.recv()
                responses.append(response)

            return responses
    except Exception as e:
        return [f"WebSocket Error: {str(e)}"]

# Main execution
if __name__ == "__main__":
    print("Fetching API data...")
    api_data = fetch_api_data()
    print("API Response:", json.dumps(api_data, indent=2))

    print("\nConnecting to WebSocket...")
    websocket_data = asyncio.run(fetch_websocket_data())
    print("WebSocket Responses:")
    for msg in websocket_data:
        print(msg)
