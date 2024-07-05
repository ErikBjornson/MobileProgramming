from kivy.app import App
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from RandomRects import RandomRects
from GridCanvas import Grid
from DraggableRect import ResizablePlate
from SampleUI import UI

Window.size = (dp(180), dp(300))

Builder.load_string('''
<MainBox@BoxLayout>:
    orientation: "vertical"
    padding: 10
    spacing: 10
    size_hint: (1, None)
    height: self.minimum_height

<Container@ScrollView>:

    scroll_timeout: 0.5
    scroll_wheel_distance: "50dp"
    
    MainBox:
        UI:
        RandomRects:
        Grid:
        ResizablePlate:
            canvas.before:
                Color:
                    rgba: (1, 1, 1, 1)
                Rectangle:
                    size: self.size
                    pos: (0, 0)
''')


class Container(ScrollView):
    pass


class Lab2App(App):
    def build(self) -> Container:
        return Container()


if __name__ == "__main__":
    Lab2App().run()
