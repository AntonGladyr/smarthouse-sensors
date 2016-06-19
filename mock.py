import websocket
import json
import time
import random

ws = websocket.WebSocket()
ws.connect('ws://127.0.0.1:3389')


static = {
    'destination': 'server',
    'type': 'sensors/init',
    'data': {
    	'air': {
    		'TRM101': {
    			'descriptions': ['testazazazazazazazaz','test','test','test','test','test','test'],
    			'values': [1,2,1,2,1,2,1]
    		},
                'TRM33': {
    			'descriptions': ['test','test','test','test','test','test','test'],
    			'values': [1,2,1,2,1,2,1]
                }
    	}
    }
    
}

ws.send(json.dumps(static))

while True:
    dynamic = {
        'destination': 'client',
        'type': 'data/dynamic',
        'data': {
    	    'air': {
    	    	'TRM101': {
    		    'descriptions': ['test','test','test'],
    		    'values': [round(random.uniform(20.0, 40.0), 3),
                        round(random.uniform(20.0, 40.0), 3),
                        round(random.uniform(20.0, 40.0), 3),]
    		},
                'TRM33': {
    		    'descriptions': ['test','test','test'],
    		    'values': [round(random.uniform(20.0, 40.0), 3),
                        round(random.uniform(20.0, 40.0), 3),
                        round(random.uniform(20.0, 40.0), 3),]
                }
    	    }
        }
    }
    ws.send(json.dumps(dynamic))
    time.sleep(1)
