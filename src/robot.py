import pybullet as p
import time
import pybullet_data
from src.interfaces.one_way_ws_interface import OneWayWPILibWSInterfaceApp

def run_sim():
    physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
    p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
    p.setGravity(0,0,-10)
    planeId = p.loadURDF("assets/plane.urdf")
    startPos = [0,0,1]
    startOrientation = p.getQuaternionFromEuler([0,0,0])
    robot = p.loadURDF("assets/my-robot/robot.urdf", startPos, startOrientation)
    # print("------")
    wheel_rad = 0.0762
    # print(p.getBodyUniqueId(robot))
    bodyUniqueID = p.getBodyUniqueId(robot)
    # for i in range(0, p.getNumJoints(robot)):
    #     print(p.getJointInfo(robot, i))
    # p.setJointMotorControlArray(bodyUniqueID, [2, 3, 1, 0], p.VELOCITY_CONTROL, targetVelocities = [100, 100, 100, 100])

    interface = OneWayWPILibWSInterfaceApp()
    # leftVel = 0
    # rightVel = 0
    timeStep = 0.015
    p.setTimeStep(timeStep)
    while True:
        startTime = time.time()
        leftVel, rightVel = interface.get_velocity()
        leftVel = leftVel / wheel_rad
        rightVel = rightVel / wheel_rad
        # print(leftVel, rightVel)
        p.setJointMotorControlArray(bodyUniqueID, [2, 3, 1, 0], p.VELOCITY_CONTROL, targetVelocities=[leftVel, leftVel, rightVel, rightVel])
        p.stepSimulation()
        print(time.time() - startTime)
        time.sleep(timeStep)
        # print(p.getJointStates(bodyUniqueID, [2, 3, 1, 0]))
        # for state in p.getJointStates(bodyUniqueID, [2, 3, 1, 0]):
        #     print(state[1])
    cubePos, cubeOrn = p.getBasePositionAndOrientation(robot)
    print(cubePos,cubeOrn)
    p.disconnect()

run_sim()