#!/usr/bin/env python

import asyncio
from websockets.server import serve

async def serve():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

async def echo(websocket):
    async for message in websocket:
        await websocket.send(youre_a(message))

serve()

#cases
#name not in db -> add character and begin playing
#name in db and already connected -> tell the user to try again
#name in db and offline -> begin playing as that character