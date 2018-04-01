import pyrebase
from pusher_push_notifications import PushNotifications
config = {
    'apiKey': "AIzaSyAhw2kHSFjIm4L3ZFbmhPCpw5mScEksDc8",
    'authDomain': "esri-eea51.firebaseapp.com",
    'databaseURL': "https://esri-eea51.firebaseio.com",
    'projectId': "esri-eea51",
    'storageBucket': "esri-eea51.appspot.com",
    'messagingSenderId': "457374308934"
  }

firebase = pyrebase.initialize_app(config)

db=firebase.database()
pn_client = PushNotifications(
    instance_id='61d2753d-9e78-4bc5-86d4-61e44fedab27',
    secret_key='1B3432CB3D025DCFB2FFC1CA9204EAB',
)


def stream_handler(message):
    print(message)
    if(message['data'] is 1):
        response = pn_client.publish(
            interests=['hello'],
            publish_body={
                'apns': {
                    'aps': {
                        'alert': 'Hello!',
                    },
                },
                'fcm': {
                    'notification': {
                        'title': 'Hello',
                        'body': 'Hello, world!',
                    },
                },
            },
        )

        print(response['publishId'])



my_stream = db.child("fire_sensor_status").stream(stream_handler,None)