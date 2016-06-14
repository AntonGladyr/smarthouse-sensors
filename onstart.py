import json


def onstart(ws, controllers):
    request = {
        'destination': 'server',
        'type': 'sensors/init',
        'data': {
            'air': {
                'TRM101': controllers['TRM101'].readStaticValues(),
                'TRM33': controllers['TRM33'].readStaticValues()
            }
        }
    }

    ws.send(json.dumps(request))
