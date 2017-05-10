import threading
from typing import List
from ObjectDetectionListener import IObjectDetectionListener
from ObjectDetectionListener import DetectedObject
from Robot import Robot
from time import sleep
import copy


class RobotBraitenbergDriver(threading.Thread, IObjectDetectionListener):
    

    def __init__(self, robot: Robot, stopEvent: threading.Event):
        threading.Thread.__init__(self)
        self.robot = robot
        self.stopEvent = stopEvent
        self.detectedObject = None
        self.noDetectionDist=0.5
        self.maxDetectionDist=0.2
        self.detectDists=[0,0,0,0,0,0,0,0]
        self.braitenbergR=[-1.6,-1.4,-1.2,-1,-0.8,-0.6,-0.4,-0.2, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        self.braitenbergL=[-0.2,-0.4,-0.6,-0.8,-1,-1.2,-1.4,-1.6, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        self.v0=2

    def objectDetected(self, detectedObjs: List[DetectedObject]):
        for d in detectedObjs:
            self.detectedObject = d

    def __objectDetected(self, detectedObj : DetectedObject):
        dist = detectedObj.dist
        index = detectedObj.sensorIndex
        print(index, dist);
        if(dist<self.noDetectionDist) :
            if (dist<self.maxDetectionDist) :
                dist=self.maxDetectionDist
            self.detectDists[index]=1-((dist-self.maxDetectionDist)/(self.noDetectionDist-self.maxDetectionDist))
        else:
            self.detectDists[index]=0
        vLeft=self.v0
        vRight=self.v0
        vLeft=vLeft+self.braitenbergL[index]*self.detectDists[index]
        vRight=vRight+self.braitenbergR[index]*self.detectDists[index]
        self.robot.move(vLeft,vRight)

    def run(self):
        self.robot.move(2,2)
        while not self.stopEvent.is_set():   
            if self.detectedObject:
                d = copy.copy(self.detectedObject)
                self.detectedObject = None
                self.__objectDetected(d)
                sleep(0.01)

