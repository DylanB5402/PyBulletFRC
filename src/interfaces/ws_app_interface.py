import websocket
import json
import time


class WPILibWSInterfaceApp:

    def __init__(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("ws://localhost:3300/wpilibws", on_message=self.on_msg)
        self.left_voltage = 0
        self.right_voltage = 0
        self.left_motor_port = '0'
        self.right_motor_port = '2'

    def on_msg(self, wsapp, message):
        data = json.loads(message)
        # print(data)
        self.get_voltage(data)
        self.send_encoder_data(687, 687)

    def get_voltage(self, data):
            # data = json.loads(self.ws.recv())
        # print(data)
        if (data['type'] == 'PWM'):
            if '<speed' in dict(data['data']).keys():
                if (data['device'] == self.left_motor_port):
                    self.left_voltage = 12 * float(data['data']['<speed'])
                elif (data['device'] == self.right_motor_port):
                    self.right_voltage = -12 * float(data['data']['<speed'])
        return (self.left_voltage, self.right_voltage)

    def send_encoder_data(self, left_count, right_count):
        # self.ws.send()
        left_encoder_data = {'data' :  {'>count' : left_count, '>period' : 0.2}, 'device': '0', 'type': 'Encoder'}
        right_encoder_data = {'data' :  {'>count' : right_count, '>period' : 0.2}, 'device': '1', 'type': 'Encoder'}
        left_encoder_data2 = {'data': {'>period': 0.2}, 'device': '0', 'type': 'Encoder'}
        right_encoder_data2 = {'data': {'>period': 0.2}, 'device': '1', 'type': 'Encoder'}
        # print(str(left_encoder_data))
        # {'data': {'>count': 687}, 'device': '0', 'type': 'Encoder'}
        # {'data': {'>count': 000}, 'device': '0', 'type': 'Encoder'}
        try:
            self.ws.send(str(left_encoder_data))
            self.ws.send(str(left_encoder_data2))
            self.ws.send(str(right_encoder_data))
            self.ws.send(str(right_encoder_data2))
            # print("sent")
            pass
        except ConnectionError:
        #     print("Error")
            pass
        time.sleep(0.02)
        pass


inter = WPILibWSInterfaceApp()
inter.ws.run_forever(skip_utf8_validation=True)
