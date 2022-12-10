from kivy.lang.builder import Builder
from kivymd.uix.widget import MDWidget
from kivymd.app import MDApp


Builder.load_file('1_label_text.kv')

class Design(MDWidget):
    pass

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Design()


Example().run()