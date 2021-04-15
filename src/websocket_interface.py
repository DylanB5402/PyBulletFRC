import websocket

class WPILibWSInterface:

    def __init__(self):
        self.ws = websocket.WebSocket()
        self.ws.connect("ws://localhost:3300/wpilibws")


