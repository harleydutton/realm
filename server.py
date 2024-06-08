#!/usr/bin/env python

import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(youre_a(message))

async def main():
    async with serve(auth, "localhost", 8765):
        await asyncio.Future()  # run forever

def youre_a(str):
    if len(str) == 0:
        return ""
    else:
        return "you're " + a_or_an(str) + str

def a_or_an(str):
    if str[0] in {'a','e','i','o','u'}:
        return "an "
    else:
        return "a "

authenticated = False
async def auth(websocket):
    async for message in websocket:
        if message == "harley":
            await websocket.send("you are harley")
            global authenticated
            authenticated = True
        elif authenticated:
            await echo(websocket)
        else:
            await websocket.send("you're not harley")

asyncio.run(main())
