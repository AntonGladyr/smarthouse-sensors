import minimalmodbus


# MODBUS & OWEN
class TRM33:
    def __init__(self):
        self.instrument = minimalmodbus.Instrument("COM4", 17)
        self.instrument.close_port_after_each_call = True


        # (address, num of decimals, function code, description)
        self.read_static_tags = [
            
        ]
        self.read_dynmaic_tags = [

        ]

    def _readValues(tags):
        result = {'values': [], 'descriptions': []}
        for tag in tags:
            result['values'].append(self.instrument.read_register(tag[0], tag[1], tag[2]))
            result['descriptions'].append(tag[3])
        return result

    def readStaticValues(self):
        return _readValues(self.read_static_tags)

    def readDynmaicValues(self):
        return _readValues(self.read_dynmaic_tags)