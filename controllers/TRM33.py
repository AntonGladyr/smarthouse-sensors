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

            [0x0000, 'Word_16', 'The numerical offset value (max) on the schedule Т.обо.го (out.)'],
            [0x0001, 'Word_16', 'The numerical offset value (min) on the schedule Т.обо.го (out.)'],
            [0x0002, 'Word_16', 'The value of the supply air temperature (Tavar.), Below which the system to frost protection mode'],
            [0x0003, 'Word_16', 'The value of the supply air temperature setpoint'],
            [0x0004, 'Word_16', 'The value of the outside temperature (summer.), In which the system to summer operation'],
            [0x0005, 'Word_16', 'The temperature Toбp. (A) schedule'],
            [0x0006, 'Word_16', 'The temperature Toбp. (A) schedule'],
            [0x0007, 'Word_16', 'The temperature Toбp. (B) schedule'],
            [0x0008, 'Word_16', 'The temperature Toбp. (B) schedule'],
            [0x0009, 'Word_16', 'The temperature Toбp. (C) schedule'],
            [0x000A, 'Word_16', 'The temperature Toбp. (C) schedule'],
            [0x000B, 'Word_16', 'The value of the dead zone in the control loop'],
            [0x0100, 'Word_16', 'Input Type TC'],    # Хх01 – ТСМ (α = 0,00426 °С -1)
                                                     # Хх02 – ТСП (α = 0,00385 °С -1)
                                                     # Хх03 – ТСП (α = 0,00391 °С -1)
                                                     # Хх04 – ТСМ (α = 0,00428 °С -1)
            [0x0101, 'Word_16', 'Input Type TC'],
            #[0x0102, 'Word_16', ''],
            [0x0103, 'Word_16', 'Code communication device with a computer'],
            [0x0104, 'Word_16', 'The time delay of the signal "Alarm" on the C2 entry when the fan is started'],

            [0x0200, 'Word_16', 'Correction value for Toutdoor'],
            [0x0201, 'Word_16', 'Correction value for Tобр'],
            [0x0202, 'Word_16', 'The correction value for the supply air.'],
            [0x0203, 'Word_16', 'The value of "filter strips" for the outside'],
            [0x0204, 'Word_16', 'The value of "filter time constant" for Tout'],
            [0x0205, 'Word_16', 'The value of "filter strips" for Tобр'],
            [0x0206, 'Word_16', 'The value of "filter time constant" for Tобр'],
            [0x0207, 'Word_16', 'The value of "filter strips" for Tsupply'],
            [0x0208, 'Word_16', 'The value of "filter time constant" for the Tsupply'],
            [0x0300, 'Word_16', 'The numerical value of S'],  #Remote Control КЗР
            [0x0301, 'Word_16', 'The coefficient τ for control'],
            [0x0302, 'Word_16', 'The value of the coefficient K for the controller'],
            [0x0303, 'Word_16', 'Warm-up Time heater'],

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
