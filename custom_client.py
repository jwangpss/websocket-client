import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"Echo: {message}")

async def main():
    start_server = websockets.serve(echo, "0.0.0.0", 8765)
    
    async with start_server:
        print("WebSocket server started on ws://0.0.0.0:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
