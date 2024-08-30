# This imports the Toga library, which is used for building the graphical user interface (GUI) application
import toga

# Button handler function is defined to handle the buttons's "on_press" event. When the button is clicked it prints "hello" to the console.
def button_handler(widget):
    print("hello")

# Build function
def build(app):
    # the toga.Box() creates a container widget that can hold other widgets.
    box = toga.Box()

# toga.Button("Hello world", on_press=button_handler) creates a button with the label "Hello world". when clicked it triggers the 'button_handler' function.
    button = toga.Button("Hello world", on_press=button_handler)
    
    # button.style.padding = 50 adds padding around the buttons text and button.style.flex = 1 makes the button expand to fill available space in its container.
    button.style.padding = 50
    button.style.flex = 1
    
    # box.add(button) adds the button to the box container
    box.add(button)

# the 'build' function returns the box, which becomes the root widget of the application window. 
    return box

# creating an instance of the toga application. The startup parameter specifies the function ('build) to call when setting up the user interface. 
def main():
    return toga.App("First App", "org.beeware.toga.tutorial", startup=build)

# this checks if the script is being run directly (not imported as a module). If so, it starts the application main event loop with 'main().main_loop()', which keeps the application running and responsive. 
if __name__ == "__main__":
    main().main_loop()