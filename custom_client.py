import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"Echo: {message}")

async def main():
    start_server = websockets.serve(echo, "192.168.1.111", 8765)
    
    async with start_server:
        print("WebSocket server started on ws://192.168.1.111:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
