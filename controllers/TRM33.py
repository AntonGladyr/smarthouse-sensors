import minimalmodbus


# MODBUS & OWEN
class TRM33:
    def __init__(self):
        self.instrument = minimalmodbus.Instrument("COM4", 17)
        self.instrument.close_port_after_each_call = True

        # (address, num of decimals, function code, description)
        self.read_static_tags = {

        }

        self.read_dynamic_tags = {

        }

    def _readValues(self, tags):
        result = {}

        for namespace, tag in tags.items():
            if namespace not in result.keys():
                result[namespace] = {'descriptions': [], 'values': []}

            # Descriptions result[namespace]['descriptions']

            # Values result[namespace]['values']

        return result

    def readStaticValues(self):
        return self._readValues(self.read_static_tags)

    def readDynamicValues(self):
        return self._readValues(self.read_dynamic_tags)
