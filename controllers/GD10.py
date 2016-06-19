import minimalmodbus
import serial

minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True


# MODBUS & OWEN
class TRM33:
    def __init__(self):
        self.instrument = minimalmodbus.Instrument("COM4", 19)
        self.instrument.mode = minimalmodbus.MODE_RTU
        self.instrument.serial.baudrate = 9600
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = serial.PARITY_NONE
        self.instrument.serial.stopbits = 1

        # (address, num of decimals, function code, description)

        self.read_static_tags = [
            [0x2000, '', 'communication control command'],
            [0x2001, '', 'communication setting frequency'],
            [0x2002, '', 'PID reference, range'],
            [0x2003, '', 'PID feedback'],
            [0x200A, '', 'Virtual input terminal command'],
            [0x200B, '', 'Virtual input terminal command'],
            [0x200D, '', 'AO output setting 1'],
            [0x2100, '', 'SW 1 of the inverter'],
            [0x2101, '', 'SW 1 of the inverter'],
            [0x2102, '', 'Fault code of the inverter'],
            [0x2103, '', 'Identifying code of the inverter']
        ]

        self.read_static_tags = [
            [0x3001, '', 'Setting frequency'],
            [0x3002, '', 'Bus voltage'],
            [0x3003, '', 'Output voltage'],
            [0x3004, '', 'Output current'],
            [0x3005, '', 'Operation speed'],
            [0x3006, '', 'Output power'],
            [0x3007, '', 'Output torque'],
            [0x3008, '', 'PID setting'],
            [0x3009, '', 'PID feedback'],
            [0x300A, '', 'Input IO state'],
            [0x300B, '', 'Output IO state'],
            [0x300C, '', 'Al 1'],
            [0x300D, '', 'Al 2']
        ]

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