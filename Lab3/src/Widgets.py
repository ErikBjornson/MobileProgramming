from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_string('''
<Box@BoxLayout>:
    orientation: "vertical"
    size_hint: (1, None)
    height: "55dp"
    padding: 20


<NumericInput@Box>:
    TextInput:
        hint_text: "Enter number..."
        input_type: "number"
        input_filter: "float"
        multiline: False
        font_size: 25


<UnpushedButton@Box>:
    Button:
        text: "Click me!"
        on_release:
            self.background_normal, self.background_down = \
                self.background_down, self.background_normal


<CheckClickButton@Box>:
    label: label
    height: "100dp"
    
    Button:
        text: "Push me!"
        on_press:
            root.label.text = "Clicked"
        on_release:
            root.label.text = "Not clicked"
    
    Label:
        id: label
        text: "Not clicked"
        font_size: 25


<CountClicksButton@Box>:
    Button:
        text: "0"
        on_release:
            self.text = str(int(self.text) + 1)


<SwitchWidget@Box>:
    switch: switch
    orientation: "horizontal"
    
    Switch:
        id: switch
        active: False

    Label:
        text: "Turned " + (lambda act: "on" if act else "off")(root.switch.active)
        font_size: 25


<SliderWidget@Box>:
    slider: slider
    height: "100dp"
    
    Slider:
        id: slider
        orientation: "horizontal"
        min: 0
        max: 100
        step: 1
    
    Label:
        text: "Current value : " + str(int(root.slider.value))
        font_size: 25
''')


class Box(BoxLayout):
    pass


class NumericInput(Box):
    pass


class UnpushedButton(Box):
    pass


class CheckClickButton(Box):
    pass


class CountClicksButton(Box):
    pass


class SwitchWidget(Box):
    pass


class SliderWidget(Box):
    pass
