from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout

Builder.load_string('''
<RandomRects@RelativeLayout>:
    size_hint: (1, None)
    height: "255dp"
    
    canvas.before:
        Color:
            rgba: (1, 1, 1, 1)
        Rectangle:
            size: (self.width, self.height)
            pos: (0, 0)
    
    canvas:
        Color:
            rgba: (1, 0, 0, 1)
        Rectangle:
            size: (self.width * 0.4, self.width * 0.4)
            pos: (0, self.height * 0.6)
        Color:
            rgba: (0, 1, 0, 1)
        Rectangle:
            size: (self.width * 0.4, self.width * 0.4)
            pos: (self.width * 0.4, self.height * 0.39)
        Color:
            rgba: (0, 0, 1, 1)
        Rectangle:
            size: (self.width * 0.4, self.width * 0.4)
            pos: (self.width * 0.6, self.height * 0.6)
    
    Label:
        text: "Square"
        font_size: 20
        font_color: (1, 0, 0, 1)
        pos_hint: {"x": 0.3, "y": 0.3}
''')


class RandomRects(RelativeLayout):
    pass
