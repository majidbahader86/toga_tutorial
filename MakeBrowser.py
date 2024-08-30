import toga
from toga.style.pack import CENTER, COLUMN, ROW, Pack

# Graze Class: This is a subclass of toga.App, which represents the main application.
# The startup method is automatically called when the app starts.
class Graze(toga.App):
    def startup(self):
        # MainWindow: Create the main application window where all content will be displayed.
        self.main_window = toga.MainWindow()

        # WebView: A widget that allows displaying web content. 
        # It takes an optional callback on_webview_load, which is triggered when a web page is loaded.
        # The style is set to flex=1, which means it will expand to fill the available space.
        self.webview = toga.WebView(
            on_webview_load=self.on_webview_loaded, style=Pack(flex=1)
        )

        # TextInput: A widget that allows users to input text. 
        # It's initialized with a default value (URL), and the style is set to flex=1 so it expands.
        self.url_input = toga.TextInput(
            value="https://beeware.org/", style=Pack(flex=1)
        )

        # Button: A button labeled "Go", which will trigger the load_page method when pressed.
        # The button's width is set to 50 and it has a left padding of 5.
        go_button = toga.Button(
            "Go",
            on_press=self.load_page,
            style=Pack(width=50, padding_left=5),
        )

        # Inner Box: A box to contain the URL input field and the Go button.
        # The box is arranged horizontally (direction=ROW) and centered with some padding around it.
        input_box = toga.Box(
            children=[
                self.url_input,
                go_button,
            ],
            style=Pack(
                direction=ROW,
                alignment=CENTER,
                padding=5,
            ),
        )

        # Outer Box: The main container box that stacks the input_box and the webview vertically (direction=COLUMN).
        # The webview takes up most of the space because of the flex=1 styling.
        box = toga.Box(
            children=[
                input_box,  # The row containing the URL input and Go button.
                self.webview,  # The WebView widget below the input row.
            ],
            style=Pack(direction=COLUMN),
        )

        # Setting the content of the main window to be our outer box.
        self.main_window.content = box

        # Setting the WebView to load the initial URL provided in the TextInput field.
        self.webview.url = self.url_input.value

        # Show the main window to the user.
        self.main_window.show()

    # load_page: This method is called when the "Go" button is pressed.
    # It updates the WebView's URL to whatever the user has typed in the TextInput field.
    def load_page(self, widget):
        self.webview.url = self.url_input.value

    # on_webview_loaded: This method is called automatically when the WebView finishes loading a page.
    # It updates the TextInput field with the actual URL of the loaded page.
    def on_webview_loaded(self, widget):
        self.url_input.value = self.webview.url


# The main function: This is the entry point of the application.
# It initializes the Graze app with a name ("Graze") and a unique identifier ("org.beeware.tutorial").
def main():
    return Graze("Graze", "org.beeware.tutorial")


# This block ensures the main function is called when the script is run directly.
# main_loop() starts the application's event loop, making the app interactive.
if __name__ == "__main__":
    main().main_loop()
