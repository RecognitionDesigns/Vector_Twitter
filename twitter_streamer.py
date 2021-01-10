import anki_vector
from anki_vector.util import degrees
import time
from PIL import Image, ImageDraw, ImageFont
from twython import TwythonStreamer
from auth import (
        API_key,
        API_secret_Key,
        Access_Token,
        Access_Token_Secret
)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            print("@{}: {}".format(username, tweet))
            face_image = Image.open('twitter.jpg')
            robot = anki_vector.AsyncRobot()
            robot.connect()

            robot.behavior.set_head_angle(degrees(30.0))
            screen_data = anki_vector.screen.convert_image_to_screen_data(face_image)
            robot.screen.set_screen_with_image_data(screen_data, 15.0, interrupt_running=True)
            say_text = robot.behavior.say_text("New Twitter Alert!, {}: {}".format(username, tweet).replace("RT", " re tweeted "))
            say_text.result()

            time.sleep(2)
            robot.disconnect()
            time.sleep(10)

stream = MyStreamer(
        API_key,
        API_secret_Key,
        Access_Token,
        Access_Token_Secret
)

print('Running')
stream.statuses.filter(track='DDL Vector, robotics, artificial intelligence')