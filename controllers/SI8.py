# -*- coding: utf8 -*-
from libs.TOwen import Owen
from libs.TSystem import MySerial

# OWEN ONLY
class SI8:
    def __init__(self):
        COM = MySerial.ComPort('COM4', 9600, timeout=0.06)
        self.instrument = Owen.OwenDevice(COM, 21)

        # (address, type, description)
        self.read_static_tags = [

        ]

        self.read_dynamic_tags = {
            'water': [
                ['DCNT', '', 'Reading pulse counter'],
                ['DSPD', '', 'Flow meter'],
                ['DTMR', '', 'Reading a timer (timer)']
            ]
        }

    def _readValues(self, tags):
        pass

    def readStaticValues(self):
        result = {'descriptions': [], 'values': []}
        for tag in self.read_static_tags:

            # Description
            result['descriptions'].append(tag[2])

            # Value
            if tag[1] == 'float24':
                result['values'].append(self.instrument.GetIEEE32(tag[0]))
            elif tag[1] == 'unsigned byte':
                result['values'].append(self.instrument.GetInt16(tag[0]))
            elif tag[1] == 'ASCII':
                result['values'].append(self.instrument.GetString(tag[0]).decode('cp1251'))
            elif tag[1] == 'unsigned short int':
                result['values'].append(self.instrument.GetInt16(tag[0]))
            else:
                result['values'].append('read error')
        return result

    def readDynamicValues(self):
        result = {}

        for namespace, tags in self.read_dynamic_tags.iteritems():
            result[namespace] = {'values': [], 'descriptions': []}
            for tag in tags:
                # Description
                result[namespace]['descriptions'].append(tag[2])

                # Value
                if tag[1] == 'float24':
                    result[namespace]['values'].append(self.instrument.GetIEEE32(tag[0]))
                elif tag[1] == 'unsigned byte':
                    result[namespace]['values'].append(self.instrument.GetInt16(tag[0]))
                elif tag[1] == 'ASCII':
                    result[namespace]['values'].append(self.instrument.GetString(tag[0]).decode('cp1251'))
                elif tag[1] == 'unsigned short int':
                    result[namespace]['values'].append(self.instrument.GetInt16(tag[0]))
                else:
                    result[namespace]['values'].append('read error')
        return result