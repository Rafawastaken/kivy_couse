import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ContainerGrid(GridLayout):
    def __init__(self, **kwargs):
        super(ContainerGrid, self).__init__(**kwargs)
        self.cols = 1

        self.top_container()
        self.bottom_container()


    # Top contaienr
    def top_container(self):        
        # Create second grid
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # Widgets
        self.top_grid.add_widget(Label(text = "Nome: ")) # Label
        self.name = TextInput(multiline = False)      
        self.top_grid.add_widget(self.name) # Text input

        self.top_grid.add_widget(Label(text = "Favorite Pizza: ")) # Label
        self.pizza = TextInput(multiline = False)      
        self.top_grid.add_widget(self.pizza) # Text input
  
        self.top_grid.add_widget(Label(text = "Favorite Color: ")) # Label
        self.color = TextInput(multiline = False)      
        self.top_grid.add_widget(self.color) # Text input

        # Add new top grid
        self.add_widget(self.top_grid)  


    # Bottom container
    def bottom_container(self):
        self.submit = Button(text = "Submit", font_size = 26) # Submit Button
        self.submit.bind(on_press = self.press) # Bind button
        self.add_widget(self.submit)


    # Press button action
    def press(self, instance):
        name = self.name.text
        color = self.color.text
        pizza = self.pizza.text

        msg = f"Hello, im {name}, my fav pizza is: {pizza} and {color}!"
        self.add_widget(Label(text = msg)) # Label

        # Clear inputs
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


# Compiler
class MyApp(App):
    def build(self):
        return ContainerGrid()


if __name__ == '__main__':
    MyApp().run()