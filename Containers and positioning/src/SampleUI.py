from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout

Builder.load_string('''
<UserButton@Button>:
    text: ""
    font_size: 30

<UserTextInput@TextInput>:
    hint_text: ""
    font_size: 30
    multiline: False
    input_type: "number"
    input_filter: "float"

<Output@Label>:
    text: "..."
    font_size: 50
    pos_hint: {"center_x": 0.5, "center_y": 0.5}

<Menu@BoxLayout>:
    orientation: "horizontal"
    padding_y: 30
    size_hint: (1, 0.2)
    pos_hint: {"center_x": 0.5, "bottom": 1}

<EntryPanel@BoxLayout>:
    orientation: "horizontal"
    padding: 30
    size_hint: (1, 0.35)
    pos_hint: {"center_x": 0.5, "top": 1}

<OutputField@BoxLayout>:
    padding: 30
    size_hint: (1, 0.3)
    pos_hint: {"center_x": 0.5, "center_y": 0.5}

<UI@RelativeLayout>:

    inp1: inp1
    inp2: inp2
    output: output
    
    size_hint: (1, None)
    height: "230dp"
    orientation: "vertical"
    
    EntryPanel:
        UserTextInput:
            id: inp1
            hint_text: "1.0"
        UserTextInput:
            id: inp2
            hint_text: "2.0"
    
    OutputField:
        Output:
            id: output
    
    Menu:
        UserButton:
            text: "Cancel"
            on_release:
                root.inp1.text = ""
                root.inp2.text = ""
                root.output.text = "..."
        UserButton:
            text: "Sum"
            on_release:
                root.output.text = str(float(root.inp1.text) + float(root.inp2.text)) \
                    if root.inp1.text != "" and root.inp2.text != "" \
                        else print("All fields must be used!")
    
''')


class UI(RelativeLayout):
    pass
