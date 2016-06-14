import json
import time


def mainloop(ws, controllers):
    while True:
        request = {
            'destination': 'client',
            'type': 'data/dynamic',
            'data': {
                'air': {}
            }
        }

        for name, controller in controllers.items():
            data = controller.readDynamicValues()
            for namespace, values in data.items():
                request['data'][namespace][name] = values

        ws.send(json.dumps(request))
        time.sleep(1)
    pass