from abc import ABC, abstractmethod
class SmartDevice(ABC):
    def show_device(self,name):
        print(name,"Device shown")
    @abstractmethod
    def turn_on(self):
        pass
class SmartLight(SmartDevice):
    def turn_on(self):
        print("Smart Light is now turned on")
class SmartFan(SmartDevice):
    def turn_on(self):
        print("Smart Fan is now turned on")
class SmartSpeaker:
    def turn_on(self):
        print("Smart Speaker is now turned on")
light=SmartLight
fan=SmartFan
speaker=SmartSpeaker
light.show_device("Car light")
light.turn_on   
fan.show_device("Bedroom Fan")
fan.turn_on
speaker.show_device("TV speaker")
speaker.turn_on
class security_camera:
    def check_status():
        print("Checking Status of security camera")
class doorlock:
    def check_status():
        print("Checking Status of door lock")
a=[security_camera(),doorlock()]
for b in a:
    b.check
