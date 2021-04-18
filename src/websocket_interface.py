import time

import websocket
import json

class WPILibWSInterface:


    def __init__(self):
        self.ws = websocket.WebSocket()
        self.ws.connect("ws://localhost:3300/wpilibws")
        self.left_voltage = 0
        self.right_voltage = 0
        self.left_motor_port = '0'
        self.right_motor_port = '2'

    def get_voltage(self):
        if (self.ws.connected):
            data = json.loads(self.ws.recv())
            print(data)
            if (data['type'] == 'PWM'):
                if '<speed' in dict(data['data']).keys():
                    if (data['device'] == self.left_motor_port):
                        self.left_voltage = 12 * float(data['data']['<speed'])
                    elif (data['device'] == self.right_motor_port):
                        self.right_voltage = -12 * float(data['data']['<speed'])
        return (self.left_voltage, self.right_voltage)

    def send_encoder_data(self, left_count, right_count):
        # self.ws.send()
        left_encoder_data = {'data' :  {'>count' : left_count}, 'device': '0', 'type': 'Encoder'}
        right_encoder_data = {'data' :  {'>count' : right_count}, 'device': '1', 'type': 'Encoder'}
        # print(str(left_encoder_data))
        # {'data': {'>count': 687}, 'device': '0', 'type': 'Encoder'}
        # {'data': {'>count': 000}, 'device': '0', 'type': 'Encoder'}
        try:
            self.ws.send(str(left_encoder_data))
            self.ws.send(str(right_encoder_data))
            print("sent")
        except ConnectionError:
            print("Error")
            pass
        time.sleep(0.001)
        pass

interface = WPILibWSInterface()
while(True):
    # print(interface.get_voltage())
    interface.get_voltage()
    interface.send_encoder_data(1000, 1000)
