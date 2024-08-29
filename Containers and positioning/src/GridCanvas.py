from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

Builder.load_string('''
<GridedObject@RelativeLayout>:
    color: 1, 1, 1, 1
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.width, self.height
            pos: 0, 0
    canvas:
        Color:
            rgba: root.color
        Rectangle:
            size: self.width*0.8, self.width*0.8
            pos: self.width*0.1, self.height*0.1

<Grid@GridLayout>:
    cols: 3
    rows: 2
    size_hint: (1, None)
    height: "180dp"
    GridedObject:
        color: 1, 0, 0, 1
    GridedObject:
        color: 0, 1, 0, 1
    GridedObject:
        color: 0, 0, 1, 1
    GridedObject:
        color: 1, 0, 1, 1
    GridedObject
    GridedObject:
        color: 0, 0, 0, 1
''')


class Grid(GridLayout):
    pass
