from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('2_slider.kv')

class MyLayout(Widget):
    def slide(self, *args):
        slider_value = str(args[1])
        self.ids.slider_label.text = str(slider_value)

class SliderApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0)
        return MyLayout()

if __name__ == '__main__':
    SliderApp().run()