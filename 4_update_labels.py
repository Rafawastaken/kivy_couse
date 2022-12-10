import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Import KV File
Builder.load_file('4_update_labels.kv')

class MyLayout(Widget):

    # Function when btn is pressed
    def press(self):
        # Variables for widgets
        name = self.ids.name_input.text
        
        # Update label
        self.ids.name_label.text = f"Hello  {name}!"

        # Clear input box
        self.ids.name_input.text = ""

class UpdateLabelApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    UpdateLabelApp().run()