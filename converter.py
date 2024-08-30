# import toga imports the Toga library for creating the GUI application
import toga

# styling- it imports the style constants and 'pack' for styling the widgets 
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack

# creating boxes- it creates container widgets to hold other widgets 
def build(app):
    c_box = toga.Box()
    f_box = toga.Box()
    box = toga.Box()

# text inputs- it creates input fields for user input
    c_input = toga.TextInput(readonly=True)
    f_input = toga.TextInput()

 # Labels- it creates labels for text display with alignment styles
    c_label = toga.Label("Celsius", style=Pack(text_align=LEFT))
    f_label = toga.Label("Fahrenheit", style=Pack(text_align=LEFT))
    join_label = toga.Label("is equivalent to", style=Pack(text_align=RIGHT))

   #Conversion logic- converts Fahrenheit to Celsius and updates 'c_input' with the result. Handles invalid input with an exception. 
    def calculate(widget):
        try:
            c_input.value = (float(f_input.value) - 32.0) * 5.0 / 9.0
        except ValueError:
            c_input.value = "???"

# Button- creates a button labeled 'calculate' that triggers the 'calculate' function when pressed.
    button = toga.Button("Calculate", on_press=calculate)

# Adding widgets- adds input fields and labels to their respective boxes
    f_box.add(f_input)
    f_box.add(f_label)
    c_box.add(join_label)
    c_box.add(c_input)
    c_box.add(c_label)

# adding boxes and button to the main box
    box.add(f_box)
    box.add(c_box)
    box.add(button)

# Styles: applies layout and spacing styles to the boxes and individual widgets
    box.style.update(direction=COLUMN, padding=10)
    f_box.style.update(direction=ROW, padding=5)
    c_box.style.update(direction=ROW, padding=5)

    c_input.style.update(flex=1)
    f_input.style.update(flex=1, padding_left=210)
    c_label.style.update(width=100, padding_left=10)
    f_label.style.update(width=100, padding_left=10)
    join_label.style.update(width=200, padding_right=10)

    button.style.update(padding=15)

    return box

# Entry point- starts the main event loop of the application if the script is run directly 
def main():
    return toga.App("Temperature Converter", "org.beeware.toga.tutorial", startup=build)


if __name__ == "__main__":
    main().main_loop()