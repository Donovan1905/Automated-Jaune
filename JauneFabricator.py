from gpiozero import Motor
from time import sleep
import sys

motorRicard = Motor(forward=4, backward=14)
motorWater = Motor(forward=5, backward=15)

motorRicard.forward()
sleep(sys.argv[1])
motorWater.forward()
sleep(sys.argv[2])
