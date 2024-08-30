import toga
from toga.style.pack import COLUMN, Pack

# button_handler: This function is triggered when a button is pressed. 
# It prints numbers 0 to 9 with a pause (yields 1), which simulates a time-consuming process.
def button_handler(widget):
    print("button handler")
    for i in range(0, 10):
        print("hello", i)
        yield 1
    print("done", i)

# actionX functions: These functions are placeholders that are associated with menu and toolbar commands. 
# When called, they print a simple message.
def action0(widget): print("action 0")
def action1(widget): print("action 1")
def action2(widget): print("action 2")
def action3(widget): print("action 3")
def action5(widget): print("action 5")
def action6(widget): print("action 6")

# Tutorial2App Class: This is a subclass of toga.App.
# The startup method is automatically called when the app starts. 
# It defines the main window, layout, and menu structure of the app.
class Tutorial2App(toga.App):
    def startup(self):
        # Icons: Setting default icons to avoid missing file warnings.
        brutus_icon = toga.Icon.DEFAULT_ICON
        cricket_icon = toga.Icon.DEFAULT_ICON

        # Table widget: left_container is a toga.Table widget showing a list of rows with headings 'Hello' and 'World'. 
        # Each row displays a pair of values from the data list.
        data = [("root%s" % i, "value %s" % i) for i in range(1, 100)]
        left_container = toga.Table(headings=["Hello", "World"], data=data)

        # Right content box: right_content is a toga.Box that holds buttons. 
        # The layout direction is set to COLUMN, meaning the buttons will be stacked vertically.
        right_content = toga.Box(style=Pack(direction=COLUMN, padding_top=50))

        # Adding Buttons: A loop adds 10 buttons to right_content, each labeled "Hello world" followed by a number.
        # The button_handler function is linked to each button's on_press event.
        for b in range(0, 10):
            right_content.add(
                toga.Button(
                    "Hello world %s" % b,
                    on_press=button_handler,
                    style=Pack(width=200, padding=20),
                )
            )

        # ScrollContainer: right_container is a scrollable container that holds right_content with the buttons.
        right_container = toga.ScrollContainer(horizontal=False)
        right_container.content = right_content

        # SplitContainer: split is a container that divides the window into two parts: 
        # left_container (the table) and right_container (the buttons). The right side is set to be twice as wide as the left.
        split = toga.SplitContainer()
        split.content = [(left_container, 1), (right_container, 2)]

        # Commands and Menus
        # Groups: Commands are organized into groups like "Things" and "Sub Menu", which define how the commands are arranged in the menu.
        things = toga.Group("Things")
        cmd0 = toga.Command(action0, text="Action 0", tooltip="Perform action 0", icon=brutus_icon, group=things)
        cmd1 = toga.Command(action1, text="Action 1", tooltip="Perform action 1", icon=brutus_icon, group=things)
        cmd2 = toga.Command(action2, text="Action 2", tooltip="Perform action 2", icon=cricket_icon, group=things)
        
        sub_menu = toga.Group("Sub Menu", parent=toga.Group.COMMANDS, order=2)
        cmd5 = toga.Command(action5, text="Action 5", tooltip="Perform action 5", order=2, group=sub_menu)
        cmd6 = toga.Command(action6, text="Action 6", tooltip="Perform action 6", order=1, group=sub_menu)

        # Special Command (cmd4): cmd4 toggles the enabled state of cmd3, demonstrating how commands can interact with each other.
        def action4(widget):
            print("CALLING Action 4")
            cmd3.enabled = not cmd3.enabled

        cmd3 = toga.Command(action3, text="Action 3", tooltip="Perform action 3", shortcut=toga.Key.MOD_1 + "k", icon=cricket_icon, order=3)
        cmd4 = toga.Command(action4, text="Action 4", tooltip="Perform action 4", icon=brutus_icon, order=1)

        # Adding Commands to the App and Toolbar
        self.commands.add(cmd1, cmd0, cmd6, cmd4, cmd5, cmd3)
        self.main_window = toga.MainWindow()

        # Adding to the Toolbar
        self.main_window.toolbar.add(cmd1, cmd3, cmd2, cmd4)
        self.main_window.content = split

        # Show Window: Finally, the window is shown to the user.
        self.main_window.show()

# Running the Application
# Entry Point: The main function initializes the Tutorial2App and starts its event loop with main_loop(), making the application interactive.
def main():
    return Tutorial2App("Tutorial 2", "org.beeware.toga.tutorial")

if __name__ == "__main__":
    main().main_loop()
