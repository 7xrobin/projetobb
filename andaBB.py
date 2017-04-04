# Thit program makes a robot moves like Jager, and take amazing shoots to analize colors in hope to find the door
#to the freedom

from Simulator import Simulator
from Robot import Robot
from time import sleep

vrep = Simulator()

vrep.connect()

robaby = Robot(vrep, "Pioneer_p3dx")

for i in range(0,300):
    robaby.update()
    robaby.drive(1,0)
    sleep(1)
vrep.disconnect()