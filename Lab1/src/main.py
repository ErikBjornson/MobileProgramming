from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Window.size = (dp(180), dp(300))

Builder.load_string('''
<Container@BoxLayout>:
    orientation: "vertical"
    padding: 30

    lbl: label
    
    Label:
        id: label
        text: "0"
        font_size: 140
        size_hint: 0.33, 0.8
        pos_hint: {"center_x": 0.5, "top": 0.5}
    BoxLayout:
        size_hint: 1, 0.2
        pos_hint: {"center_x": 0.5, "bottom": 0.5}
        Button:
            text: "+"
            font_size: 40
            on_press: root.lbl.text = str(int(root.lbl.text) + 1)
        Button:
            text: "-"
            font_size: 40
            on_press: root.lbl.text = str(int(root.lbl.text) - 1)
        Button:
            text: "Reset"
            font_size: 40
            on_press: root.lbl.text = "0"
''')

 
class Container(BoxLayout):
    pass


class Lab1App(App):
    def build(self) -> Container:
        return Container()


if __name__ == '__main__':
    Lab1App().run()
