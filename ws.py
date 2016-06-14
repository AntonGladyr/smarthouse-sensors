import websocket


class WebSocket:
    def __init__(self, url, controllers):
        self.ws = websocket.WebSocketApp(url,
                                         on_message=self.on_message)

    def on_message(self, ws, msg):
        pass

    def run(self):
        self.ws.run_forever()
