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
        self.read_static_tags = [
            [0x145, 'Word_16', 'The reason for the latter unit program start'],  # only read 0 - decrease power;
            #           1 - switch power;
            #           3 - watchdog timer;
            #           6 - Exhaustion stack;
            #           7 - overflow stack
            [0x039B, 'Byte', 'Code of the last network errors'],  # only read 0 after start
            [0x03AF, 'Word_16', 'Bit per second'],  # read/write  0 - 2.4 kbit / s;
            #             1 - 4.8 kbit / s;
            #             2 - 9.6 kbit / s;
            #             3 - 14.4 kbit / s;
            #             4 - 19.2 kbit / s;
            #             5 - 28.8 kbit / s;
            #             6 - 38.4 kbit / s;
            #             7 - 57,6 kbit / s;
            #             8 - 115.2 kbit / s

            [0x03B0, 'Word_16', 'Type of parity'],  # read/write  0 - no control;
            #             1 - parity;
            #             2 - Odd

            [0x03B1, 'Word_16', 'Number of stop bits'],  # read/write  0 - one
            [0x03B5, 'Word_16', 'Response delay'],  # read/write  0...50 ms
            [0x03B2, 'Word_16', 'device address'],  # read/write  1...247
            [0x0478, 'Word_16', 'Recording changes in EEPROM and restructuring UART'],  # only write

            [0x02BC, 'Float_32/multipleRegisters', 'The numerical offset value (Δmax)'],
            [0x02C0, 'Float_32/multipleRegisters', 'The value of the supply air temperature (product)'],
            [0x02C4, 'Float_32/multipleRegisters', 'Setpoint for supply air'],
            [0x02C8, 'Float_32/multipleRegisters', 'The permitted value of lowering the return water temperature']
        ]

        self.read_dynamic_tags = {
            'air': [
                [0x0080, 'Float_32', 'The measured value of the outdoor air temperature'],
                [0x0084, 'Float_32', 'The measured value of the supply air temperature'],
            ],
            'water': [
                [0x0082, 'Float_32', 'The measured value of the return water temperature']
            ]
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
