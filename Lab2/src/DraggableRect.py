from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Rectangle

pad: int = 10
space: int = 10
h: float = dp(255)


class DraggableRectangle(Widget):
    def __init__(self, **kwargs) -> None:
        super(DraggableRectangle, self).__init__(**kwargs)
        self.offset: list[int] = []
        self.prev_touch_pos: list[int] = []
        with self.canvas.before:
            Color(1, 0, 0, 1)
            self.rect = Rectangle(size=(100, 100), pos=(0, 0))
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args) -> None:
        self.rect.pos = self.pos

    def on_touch_down(self, touch) -> bool:
        if self.collide_point(*touch.pos):
            self.offset = [touch.x - self.x, touch.y - self.y]
            self.prev_touch_pos = touch.pos
            touch.grab(self)
            return True
        return super(DraggableRectangle, self).on_touch_down(touch)

    def on_touch_move(self, touch) -> bool:
        if touch.grab_current is self:
            new_x: int = touch.x - self.offset[0]
            new_y: int = touch.y - self.offset[1]
            right_bound: int = Window.width - self.rect.size[0] - (pad + space)
            top_bound: int = h - self.rect.size[1]
            if 0 < new_x < right_bound and 0 < new_y < top_bound:
                self.pos = [new_x, new_y]
                self.prev_touch_pos = touch.pos
        return super(DraggableRectangle, self).on_touch_move(touch)

    def on_touch_up(self, touch) -> None:
        if touch.grab_current is self:
            touch.ungrab(self)
        return super(DraggableRectangle, self).on_touch_up(touch)


class ResizablePlate(RelativeLayout):
    def __init__(self, **kwargs) -> None:
        super(ResizablePlate, self).__init__(**kwargs)
        self.size_hint = (1, None)
        self.height = h
        self.rect: DraggableRectangle = DraggableRectangle(size_hint=(0.25, 0.25))
        self.rect.pos = (
            self.width / 2 + self.rect.width * 0.92,
            self.height / 2 - self.rect.height / 2
        )
        self.add_widget(self.rect)
