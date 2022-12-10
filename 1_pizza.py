import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


# Link KV fIle
Builder.load_file('1_pizza.kv')

class ContainerGrid(Widget):
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)


    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(name, pizza, color)

        # Clear inputs
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

# Compiler
class KivyApp(App):
    def build(self):
        return ContainerGrid()


if __name__ == '__main__':
    KivyApp().run()