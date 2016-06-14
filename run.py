from controllers.TRM101 import TRM101
from controllers.TRM33 import TRM33

import threading

from ws import WebSocket
from mainloop import mainloop
from onstart import onstart

HOST = "ws://10.1.212.78:3389"

controllers = {
    'TRM33': TRM33(),
    'TRM101': TRM101(),

}

websocket = WebSocket(HOST, controllers)
threading.Thread(target=websocket.run).start()

onstart(websocket, controllers)
mainloop(websocket, controllers)
