from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('1_round.kv')

class MyLayout(Widget):
    pass

class RoundApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()

if __name__ == '__main__':
    RoundApp().run()