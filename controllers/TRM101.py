# -*- coding: utf8 -*-
from libs.TOwen import Owen
from libs.TSystem import MySerial


# OWEN ONLY
class TRM101:
    def __init__(self):
        COM = MySerial.ComPort('COM4', 9600, timeout=1)
        self.instrument = Owen.OwenDevice(COM, 17)

        # (address, type, description)
        self.read_static_tags = [
            ['SP', 'float24', 'Controller set point'],
            ['r-S', 'unsigned byte', 'Start/stop control'],     # StoP -> 0; rUn -> 1
            ['At', 'unsigned byte', 'Start/stop autoconfig'],   # StoP -> 0; rUn -> 1
            ['in-t', 'unsigned byte', 'Input sensor or signal type'], #r385     ->   1
                                                                      #r.385    ->   2
                                                                      #r391	    ->   3
                                                                      #r.391    ->   4
                                                                      #r-21	    ->   5
                                                                      #r426	    ->   6
                                                                      #r.426    ->   7
                                                                      #r-23	    ->   8
                                                                      #r428	    ->   9
                                                                      #r.428    ->	 10
                                                                      #E-A1	    ->   11
                                                                      #E-A2	    ->   12
                                                                      #E-A3	    ->   13
                                                                      #E__b	    ->   14
                                                                      #E__j	    ->   15
                                                                      #E__K	    ->   16
                                                                      #E__L	    ->   17
                                                                      #E__n	    ->   18
                                                                      #E__r	    ->   19
                                                                      #E__S	    ->   20
                                                                      #E__t	    ->   21
                                                                      #i0_5	    ->   22
                                                                      #i0.20	->   23
                                                                      #i4.20	->   24
                                                                      #U-50	    ->   25
                                                                      #U0_1	    ->   26

            ['dPt', 'unsigned byte', 'Temperature output accuracy'],
            ['dP', 'unsigned byte', 'Decimal point position'],
            ['in-L', 'float24', 'The lower limit of the measuring range'],
            ['in-H', 'float24', 'The upper limit of the measuring range'],
            ['SL-L', 'float24', 'The lower limit setpoint'],
            ['SL-H', 'float24', 'The upper limit setpoint'],
            ['SH', 'float24', 'Shift sensor characteristics'],
            ['KU', 'float24', 'Tilt sensor characteristics'],
            ['inF', 'float24', 'Filter constant'],
            ['Fb', 'float24', 'Band digital filter'],
            ['An-L', 'float24', 'The lower limit of the range of the DAC2 register'],
            ['An-H', 'float24', 'The upper limit of the range of the DAC register'],
            ['Ev-1', 'unsigned byte', 'Key feature auxiliary input'], # nonE ->  0
                                                                      # n-o	->  1
                                                                      # n-C	->  2
            ['ALt', 'unsigned byte', 'Type comparator logic'],
            ['AL-d', 'float24', 'Comparator threshold'],
            ['AL-Н', 'float24', 'Comparator hysteresis'],
            ['orEU', 'unsigned byte', 'Type in the regulation control'], # or-r	 ->  0
                                                                         # or-d	 ->  1
            ['CP', 'unsigned byte', 'The repetition period of the control pulses'],
            ['vSP', 'float24', 'Speed setpoint changes'],
            ['cntL', 'unsigned byte', 'Regulatory regime'],
            ['HYST', 'float24', 'Hysteresis off controller'],
            ['onSt', 'unsigned byte', 'Output state "control stop" mode'], # oFF  ->  0
                                                                           # on	  ->  1
            ['onEr', 'unsigned byte', 'Output state "error" mode'], # oFF  -> 	0
                                                                    # on   ->	1
            ['ramP', 'unsigned byte', 'Mode "quick access to the setpoint"'], # oFF  ->  0
                                                                              # on	 ->  1
            ['P', 'float24', 'Proportional band of PID'],
            ['i', 'float24', 'Integral constant PID'],
            ['d', 'float24', 'Differential constant PID'],
            ['db', 'float24', 'Deadband PID'],
            ['oL-L', 'float24', 'Minimum Power Output (lower limit)'],
            ['oL-H', 'float24', 'Maximum power output (the upper limit)'],
            ['orL', 'float24', 'The maximum output power of the rate of change'],
            ['mvEr', 'float24', 'Output power value in a state of "error"'],
            ['mvSt', 'float24', 'The value of the output power in the state "control stop'],
            ['mdSt', 'unsigned byte', 'Output state "control stop" mode'], # mvSt ->  0
                                                                           # o	  ->  1
            ['LBA', 'unsigned short int', 'Diagnosis time of open circuit'],
            ['LbAb', '', 'Band width of diagnosis time of open circuit'],

            # network settings of device
            #----------- Network settings of device --------------------------
            ['Addr', 'unsigned short int', 'The base address of the device on the network'],
            ['rSdL', 'unsigned byte', 'Delay in answering via RS-485'],
            ['A.LEn', 'unsigned byte', 'Network Address Length'], # 8b	 ->  0
                                                                  # 11b	 ->  1

            ['bPS', 'unsigned byte', 'The speed of the network sharing'], # 2.4    ->	0
                                                                          # 4.8    ->	1
                                                                          # 9.6    ->	2
                                                                          # 14.4   ->   3
                                                                          # 19.2   ->   4
                                                                          # 28.8   ->   5
                                                                          # 38.4   ->   6
                                                                          # 57.6   ->   7
                                                                          # 115.2  ->   8
            #----------- Network settings of device --------------------------

            #----------- Group service parameters ----------------------------
            ['LEn', 'unsigned byte', 'Data word length'], # 8  ->  1
            ['PrtY', 'unsigned byte', 'Status bit parity in the parcel'], # nonE  ->  0
            ['Sbit', 'unsigned byte', 'Number of stop bits per parcel'],  # 1  ->  0
            ['VER', 'ASCII', 'Software version'],
            ['Dev', 'ASCII', 'Device Type'],
            ['APLY', '', 'Team transition to the new network settings'],
            ['INIT', '', 'Team reboot the device. Equivalent off / on power'],
            ['N.err', 'unsigned short int', ''], # Код сетевой ошибки при последнем обращении:
                                                 # 0х06 - Значение мантиссы превышает ограничения дескриптора
                                                 # 0x08 - У запрошенного параметра отсутствуют атрибуты
                                                 # 0х28   –  Не найден дескриптор
                                                 # 0х31   –  Размер поля данных не соответствует  ожидаемому
                                                 # 0х32   – Значение бита запроса не соответствует  ожидаемому
                                                 # 0х33   –  Редактирование параметра запрещено  индивидуальным атрибутом
                                                 # 0х34   –  Недопустимо большой линейный индекс
                                                 # 0х47   –  Недопустимое сочетание значений параметров
                                                 #           (Редактирование параметра заблокировано  значением другого или значениями нескольких  других)
                                                 # 0х48   –  Ошибка при чтении EEPROM (ответ при наличии Er.64)
            #----------- Group service parameters --------------------------

            #----------- Teams set attributes ------------------------------
            ['Attr', '', 'To read / write attribute of "editing"'],
            #----------- Teams set attributes ------------------------------

            #----------- Group LmAn (manual control) -----------------------  Виден при  CNTL = PID, R−S = RUN, AT = STOP
            ['o-Ed', 'float24', 'Set point of output power'],
            #----------- Group LmAn (manual control) -----------------------

            #----------- privacy settings -----------------------   (группа скрыта под паролем PASS=100)
            ['EdPt', 'unsigned byte', 'Protecting the individual parameters of the review and the changes(enable or disable the action attribute)']
            #----------- privacy settings -----------------------
        ]

        self.read_dynamic_tags = [
            ['PV', 'float24', 'The measured value of the input variable or an error code'], # - 0xFD-error at the input
                                                                                            # - 0xFE - lack of communication with the ADC
                                                                                            # - 0xF0 - the calculated value is certainly not true
                                                                                            # (Answer in the presence of Er.64)
            ['o', 'float24', 'Output power of PID.'],
            ['o.', 'float24', 'The current value of the output PID']
        ]

    def _readValues(self, tags):
        result = {'values': [], 'descriptions': []}

        for tag in tags:

            # Description
            result['descriptions'].append(tag[2])

            # Value
            if tag[1] == 'float24':
                result['values'].append(self.instrument.GetIEEE32(tag[0]))
            elif tag[1] == 'unsigned byte':
                result['values'].append(self.instrument.GetInt16(tag[0]))
            elif tag[1] == 'ASCII':
                result['values'].append(self.instrument.GetString(tag[0]))
            elif tag[1] == 'unsigned short int':
                result['values'].append(self.instrument.GetInt16(tag[0]))

        return result

    def readStaticValues(self):
        return self._readValues(self.read_static_tags)

    def readDynamicValues(self):
        return self._readValues(self.read_dynamic_tags)
