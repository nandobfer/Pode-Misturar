from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)

class SumSymbol(Widget):
    pass

class InputsContainers(Widget):
    pass

class Input_1(Widget):
    pass

class Input_2(Widget):
    pass

class Background(Widget):
    pass

class PodeMisturar(App):
    screen_height = NumericProperty(1)
    def build(self):
        self.root = root = Background()
        self.screen_height = 640
        return root


if __name__ == '__main__':
    PodeMisturar().run()
    
