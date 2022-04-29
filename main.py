from kivy.app import App
from kivy.uix.button import Button
import requests

def press_button(instance):
    print("pressed", instance.text)
    requests.post("https://imageserver.robinskaba.repl.co/ping")

class TestApp(App):
    def build(self):
        btn = Button(text="Hello World")
        btn.bind(on_press=press_button)
        return btn

TestApp().run()