import websocket
import json
import time


class OneWayWPILibWSInterfaceApp:

    def __init__(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("ws://localhost:3300/wpilibws", on_message=self.on_msg)
        self.left_velocity = 0
        self.right_velocity = 0
        self.left_motor_port = '0'
        self.right_motor_port = '2'

    def on_msg(self, wsapp, message):
        data = json.loads(message)
        self.process_data(data)
        print(self.left_velocity, self.right_velocity)
    def process_data(self, data):
        if (data['device'] == 'DriveData'):
            if ('>left_vel_mps' in data['data']):
                self.left_velocity = float(data['data']['>left_vel_mps'])
            elif ('>right_vel_mps' in data['data']):
                self.right_velocity = float(data['data']['>right_vel_mps'])

inter = OneWayWPILibWSInterfaceApp()
inter.ws.run_forever()