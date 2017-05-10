from Robot import Robot
import threading


class OdometryRobot():
	'''
	This class calcule odometry of robot by the angular position of the whells
	given by the encoder
	'''
	def __init__(self, robot: Robot, stopEvent: threading.Event):
	    # threading.Thread.__init__(self)
	    self.robot = robot
	    self.stopEvent = stopEvent
	    self.lastEncoder = [0] * 2
	    self.whellVelocity = [0]*2

	def newAngularPosition(self):
		left = self.__getAngleDiff(self.robot.encoder[0] , self.lastEncoder[0])
		right = self.__getAngleDiff(self.robot.encoder[1] , self.lastEncoder[1])
		
		self.__calcAngularVelocity(left, right)

		self.lastEncoder[0] = self.robot.encoder[0]
		self.lastEncoder[1] = self.robot.encoder[1]
		self.robot.lastTimeRead = self.robot.encoderReadTime

	def __calcAngularVelocity(self, left, right):
		time = (self.robot.encoderReadTime - self.robot.lastTimeRead)/1000
		self.whellVelocity[0] = left / time
		self.whellVelocity[1] = right / time
		print("left dist: ", left," right: ", right, " time: ", time, " veloLef: ", self.whellVelocity[0], " veloRight: ", self.whellVelocity[1])


	 #a1= new angle, a2 =last angle
	def __getAngleDiff(self, a1,a2):
		if (a1 >= 0 and a2 >= 0):
			return a1 - a2
		elif (a1 < 0 and a2 >=0):
			return a2 - (a1 * -1)
		elif (a1 < 0 and a2 < 0):
			return a1 - a2
		elif (a1 >= 0 and a2 < 0):
			return a1 - (a2 * -1)
		return 0
