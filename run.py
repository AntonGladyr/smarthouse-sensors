from controllers.TRM101 import TRM101
from controllers.TRM33 import TRM33
from ws import WebSocket
import threading
from mainloop import mainloop

HOST = "ws://smarthouse.onlini.co:3389"

controllers = [
    TRM101(),
    TRM33()
]

websocket = WebSocket(HOST, controllers)
threading.Thread(target=websocket.run).start()
mainloop(websocket, controllers)