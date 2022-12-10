from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Load KV file for UI
Builder.load_file('5_calculator.kv')

# Set app size
Window.size = (500, 700)

class CalculatorLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    # Button press
    def button_press(self, button):
        prev = self.ids.calc_input.text

        if "ERROR" in prev:
            prev = ''

        # Check if content
        if prev == "0":
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prev}{button}"


    # Addition function
    def sign(self, sign):
        prev = self.ids.calc_input.text
        
        # Add plus sign
        self.ids.calc_input.text = f"{prev}{sign}"


    # Calculate result function
    def equals(self):
        prev = self.ids.calc_input.text
        try:
            result = eval(prev)
            self.ids.calc_input.text = str(result)
        except:
            self.ids.calc_input.text = "ERROR"


    
    # Decimal Dott
    def dot(self):
        prev = self.ids.calc_input.text

        num_list = prev.split('+')

        if "+" in prev and "." not in num_list[-1]:
            prev = f'{prev}.'
            self.ids.calc_input.text = prev

        elif "." not in prev:
            prev = f'{prev}.'
            self.ids.calc_input.text = prev



    def delete(self):
        self.ids.calc_input.text = self.ids.calc_input.text[:-1]

    def pos_neg(self):
        prev = self.ids.calc_input.text
        if '-' in prev:
            self.ids.calc_input.text = prev.replace('-', "")
        else:
            self.ids.calc_input.text = f"-{prev}"


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == '__main__':
    CalculatorApp().run()