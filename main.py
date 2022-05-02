import requests
from kivy.app import App
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
import numpy as np
import cv2

def call_request():
    print("calling request")
    response = requests.get("https://kivyhost.robinskaba.repl.co/askforscreenshot")
    nparr = np.frombuffer(response.content, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite("result.jpg", img)

class Widget2(ButtonBehavior, Image):
    def __init__(self):
        super().__init__()
        self.source = "gasai.jpg"

    def on_press(self):
        print("pressed")
        call_request()
        self.reload()
        self.source = "result.jpg"

class MyApp(BoxLayout, App):
    def build(self):
        self.add_widget(Widget2())
        return self

MyApp().run()
