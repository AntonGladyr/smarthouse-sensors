from libs.TOwen import Owen
from libs.TSystem import MySerial
import minimalmodbus
import serial

# COM = MySerial.ComPort('COM4', 9600, timeout=1)
# instrument = Owen.OwenDevice(COM, 17)

minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True

instrument = minimalmodbus.Instrument("COM4", 18)
instrument.mode = minimalmodbus.MODE_RTU
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
