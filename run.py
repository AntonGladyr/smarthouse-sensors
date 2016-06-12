from controllers.TRM101 import TRM101
from controllers.TRM33 import TRM33

import threading

from ws import WebSocket
from mainloop import mainloop
from onstart import onstart

HOST = "ws://smarthouse.onlini.co:3389"

controllers = {
    'TRM101': TRM101(),
    'TRM33': TRM33()
}

websocket = WebSocket(HOST, controllers)
threading.Thread(target=websocket.run).start()

onstart(websocket, controllers)
mainloop(websocket, controllers)
