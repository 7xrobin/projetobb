from Simulator import Simulator
from Robot import Robot
from RobotMonitor import RobotMonitor
from time import sleep
# from plotrobot import plotRobotAndObjects
import threading
from ObjectDetectionListener import PrinterObjectDetectionListener
from PositionListener import PrinterPositionListerner
from RobotDummyDriver import RobotDummyDriver
# from RobotBraitenbergDriver import RobotBraitenbergDriver
from OdometryRobot import OdometryRobot


def main():
    sim = Simulator()
    sim.connect()

    stopEvent = threading.Event()

    robot = Robot(sim, "Pioneer_p3dx")
    odometrator = OdometryRobot(robot, stopEvent)
    monitor = RobotMonitor(robot, odometrator, stopEvent)

    driver = RobotDummyDriver(robot, stopEvent)
    # driver = RobotBraitenbergDriver(robot, stopEvent)

    monitor.subscribeToFrontObjectDetection(driver)

    driver.start()
    monitor.start()

    # plotThread = threading.Thread(target=plotRobotAndObjects, args=(monitor,))
    # plotThread.start()

    try:
        while monitor.is_alive():
            monitor.join(timeout=1.0)
            driver.join(timeout=1.0)
    except (KeyboardInterrupt, SystemExit):
        stopEvent.set()
    
    # plotThread.join()
    sim.disconnect()

if __name__ == '__main__':
    main()