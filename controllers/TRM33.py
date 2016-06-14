import minimalmodbus
import serial
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True


# MODBUS & OWEN
class TRM33:
    def __init__(self):
        self.instrument = minimalmodbus.Instrument("COM4", 18)
        self.instrument.mode = minimalmodbus.MODE_RTU
        self.instrument.serial.baudrate = 9600
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = serial.PARITY_NONE
        self.instrument.serial.stopbits = 1

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
