#!/usr/bin/env python

from websockets.sync.client import connect

#python -m websockets ws://localhost:8765/

host = "ws://localhost:8765"

with connect(host) as websocket:
    websocket.send()

def hello():
    with connect("ws://localhost:8765") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")





