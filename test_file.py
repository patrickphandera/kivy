import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import kivy
kivy.require('1.9.0')

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
from kivy.core.window import Window
class Layout(GridLayout):
    def __init__(self):
        super(GridLayout, self).__init__()
    def close(self):
            App.get_running_app().stop()
class mamdouh(App):

    def build(self):
        return Layout

if __name__ == '__main__':
    app = mamdouh()
    app.run()
    