import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Import KV File
Builder.load_file('2_bg.kv')

class MyLayout(Widget):
    pass

class BoxLayoutApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    BoxLayoutApp().run()