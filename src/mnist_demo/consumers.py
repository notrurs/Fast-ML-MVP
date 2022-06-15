import json
from io import BytesIO
from base64 import b64decode

from channels.generic.websocket import WebsocketConsumer

from .services import model


class AppConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        image = json.loads(text_data)['image']
        prediction = model.predict(BytesIO(b64decode(image)))
        response = {
            'data': {
                'prediction': prediction,
                'predicted_num': max(prediction, key=prediction.get)
            }
        }
        self.send(text_data=json.dumps(response))
