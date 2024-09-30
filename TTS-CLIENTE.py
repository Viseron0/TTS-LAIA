import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8765"
    
    async with websockets.connect(uri) as websocket:
        # Envía un mensaje para iniciar la consulta
        await websocket.send("Iniciar consulta")
        
        # Recibe la respuesta del servidor
        response = await websocket.recv()
        print(f"Respuesta del servidor: {response}")

asyncio.get_event_loop().run_until_complete(send_message())
