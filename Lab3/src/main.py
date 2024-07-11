from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from Widgets import *

Window.size = (dp(180), dp(300))

Builder.load_string('''
<MainBox@BoxLayout>:
    orientation: "vertical"
    padding: 30
    size_hint: (1, None)
    height: self.minimum_height

<Container@ScrollView>:

    scroll_timeout: 0.5
    scroll_wheel_distance: "50dp"
    
    MainBox:
        NumericInput:
        UnpushedButton:
        CheckClickButton:
        CountClicksButton:
        SwitchWidget:
        SliderWidget:
''')


class Container(ScrollView):
    pass


class Lab3App(App):
    def build(self) -> Container:
        return Container()


if __name__ == "__main__":
    Lab3App().run()
