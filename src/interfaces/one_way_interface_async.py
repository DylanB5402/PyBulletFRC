import websocket
import json
import time


class OneWayWPILibWSInterfaceApp:

    def __init__(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocket()
        self.ws.connect("ws://localhost:3300/wpilibws")
        self.left_velocity = 0
        self.right_velocity = 0
        # self.left_motor_port = '0'
        # self.right_motor_port = '2'

    async def get_velocity(self):
        data = json.loads(self.ws.recv())
        if (data['device'] == 'DriveData'):
            if ('>left_vel_mps' in data['data']):
                self.left_velocity = float(data['data']['>left_vel_mps'])
            elif ('>right_vel_mps' in data['data']):
                self.right_velocity = float(data['data']['>right_vel_mps'])
        return (self.left_velocity, self.right_velocity)

