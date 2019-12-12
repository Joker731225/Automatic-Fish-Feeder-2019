from gpiozero import LED
from time import sleep

# the relay is connected to GPIO pin 18 on the Raspberry Pi
 # replace the 18 below with whatever pin is appropriate for your
 # hardware setup
relay = LED(18)

# the following is an infinite loop in Python, it runs until you
 # kill the application
while True:
 # turn the relay on
 relay.on()
 # wait a second
 sleep(2)
 # turn the relay off
 relay.off()
 # wait another second
 # this wait time can be adjusted based upon the quantity of fish and 
 #often you want the fish to be fed
 # one day is eighty-six thousand, four hundred seconds.
 # to find twelve hours, divide the above number by two. 
 sleep(86400)
