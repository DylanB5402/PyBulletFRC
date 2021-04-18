import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("assets/plane.urdf")
startPos = [0,0,1]
startOrientation = p.getQuaternionFromEuler([0,0,0])
robot = p.loadURDF("assets/my-robot/robot.urdf", startPos, startOrientation)
print("------")
# print(p.getBodyUniqueId(robot))
bodyUniqueID = p.getBodyUniqueId(robot)
# for i in range(0, p.getNumJoints(robot)):
#     print(p.getJointInfo(robot, i))
# p.setJointMotorControlArray(bodyUniqueID, [2, 3, 1, 0], p.VELOCITY_CONTROL, targetVelocities = [100, 100, 100, 100])
while True:
    p.setJointMotorControlArray(bodyUniqueID, [2, 3, 1, 0], p.VELOCITY_CONTROL, targetVelocities=[100, 100, 100, 100])
    p.stepSimulation()
    time.sleep(1./240.)
    # print(p.getJointStates(bodyUniqueID, [2, 3, 1, 0]))
    # for state in p.getJointStates(bodyUniqueID, [2, 3, 1, 0]):
    #     print(state[1])
cubePos, cubeOrn = p.getBasePositionAndOrientation(robot)
print(cubePos,cubeOrn)
p.disconnect()
