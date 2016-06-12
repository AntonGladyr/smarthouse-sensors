import minimalmodbus


# MODBUS & OWEN
class TRM33:
    def __init__(self):
        self.instrument = minimalmodbus.Instrument("COM4", 17)
        self.instrument.close_port_after_each_call = True

        # (address, num of decimals, function code, description)
        self.read_static_tags = [

        ]
        self.read_dynamic_tags = [

        ]

    def _readValues(self, tags):
        result = {'values': [], 'descriptions': []}
        for tag in tags:
            # TODO: Modbus read values
            pass
        return result

    def readStaticValues(self):
        return self._readValues(self.read_static_tags)

    def readDynmaicValues(self):
        return self._readValues(self.read_dynamic_tags)
