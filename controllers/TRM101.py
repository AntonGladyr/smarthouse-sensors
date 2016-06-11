from libs.TOwen import Owen
from libs.TSystem import MySerial

# OWEN ONLY
class TRM101:
    def __init__(self):
        COM = MySerial.ComPort(4, 9600, timeout=1)
        self.instrument = Owen.OwenDevice(COM, 17)

        # (address, type, description)
        self.read_static_tags = [
            
        ]

        self.read_dynamic_tags = [
            
        ]

    def _readValues(self, tags):
        result = {'values': [], 'descriptions': []}
        for tag in tags:
            # TODO: Owen read values
            pass
        return result

    def readStaticValues(self):
        pass

    def readDynamicValues(self):
        pass
