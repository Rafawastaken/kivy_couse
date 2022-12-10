from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen


# Different screens
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('3_screen_manager.kv')


class ScreenManagerApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0)
        return kv

if __name__ == '__main__':
    ScreenManagerApp().run()