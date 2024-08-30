import math

import toga
from toga.colors import WHITE, rgb
from toga.constants import Baseline
from toga.fonts import SANS_SERIF
from toga.style import Pack

# StartApp Class: This class is a subclass of toga.App, which is the main application class.
# The startup method is called automatically when the app starts.
class StartApp(toga.App):
    def startup(self):
        # Create the main application window with a specific size.
        self.main_window = toga.MainWindow(size=(150, 250))

        # Create an empty canvas that will be used to draw the image.
        # The canvas can resize, and it has handlers for resize and press events.
        self.canvas = toga.Canvas(
            style=Pack(flex=1),
            on_resize=self.on_resize,
            on_press=self.on_press,
        )

        # Create a box layout to hold the canvas.
        box = toga.Box(children=[self.canvas])

        # Set the content of the main window to be the box containing the canvas.
        self.main_window.content = box

        # Draw the image of Tiberius the yak on the canvas.
        self.draw_tiberius()

        # Display the main window to the user.
        self.main_window.show()

    # fill_head Method: This method draws and fills the head of Tiberius on the canvas.
    def fill_head(self):
        with self.canvas.Fill(color=rgb(149, 119, 73)) as head_filler:
            # Draw the lower part of the head
            head_filler.move_to(112, 103)
            head_filler.line_to(112, 113)
            head_filler.ellipse(73, 114, 39, 47, 0, 0, math.pi)  # Draw chin
            head_filler.line_to(35, 84)
            # Draw the left and right curves of the head
            head_filler.arc(65, 84, 30, math.pi, 3 * math.pi / 2)
            head_filler.arc(82, 84, 30, 3 * math.pi / 2, 2 * math.pi)

    # stroke_head Method: This method draws the outline of Tiberius' head on the canvas.
    def stroke_head(self):
        with self.canvas.Stroke(line_width=4.0) as head_stroker:
            with head_stroker.ClosedPath(112, 103) as closed_head:
                closed_head.line_to(112, 113)
                closed_head.ellipse(73, 114, 39, 47, 0, 0, math.pi)
                closed_head.line_to(35, 84)
                closed_head.arc(65, 84, 30, math.pi, 3 * math.pi / 2)
                closed_head.arc(82, 84, 30, 3 * math.pi / 2, 2 * math.pi)

    # draw_eyes Method: This method draws the eyes of Tiberius on the canvas.
    def draw_eyes(self):
        with self.canvas.Fill(color=WHITE) as eye_whites:
            eye_whites.arc(58, 92, 15)  # Draw left eye white
            eye_whites.arc(88, 92, 15, math.pi, 3 * math.pi)  # Draw right eye white

        # Draw the outlines of the eyes.
        with self.canvas.Stroke(line_width=4.0) as eye_outline:
            eye_outline.arc(58, 92, 15)  # Draw left eye outline
        with self.canvas.Stroke(line_width=4.0) as eye_outline:
            eye_outline.arc(88, 92, 15, math.pi, 3 * math.pi)  # Draw right eye outline

        # Draw the pupils of the eyes.
        with self.canvas.Fill() as eye_pupils:
            eye_pupils.arc(58, 97, 3)  # Draw left pupil
            eye_pupils.arc(88, 97, 3)  # Draw right pupil

    # draw_horns Method: This method draws the horns of Tiberius on the canvas.
    def draw_horns(self):
        # Draw the right horn.
        with self.canvas.Context() as r_horn:
            with r_horn.Fill(color=rgb(212, 212, 212)) as r_horn_filler:
                r_horn_filler.move_to(112, 99)
                r_horn_filler.quadratic_curve_to(145, 65, 139, 36)
                r_horn_filler.quadratic_curve_to(130, 60, 109, 75)
            with r_horn.Stroke(line_width=4.0) as r_horn_stroker:
                r_horn_stroker.move_to(112, 99)
                r_horn_stroker.quadratic_curve_to(145, 65, 139, 36)
                r_horn_stroker.quadratic_curve_to(130, 60, 109, 75)

        # Draw the left horn.
        with self.canvas.Context() as l_horn:
            with l_horn.Fill(color=rgb(212, 212, 212)) as l_horn_filler:
                l_horn_filler.move_to(35, 99)
                l_horn_filler.quadratic_curve_to(2, 65, 6, 36)
                l_horn_filler.quadratic_curve_to(17, 60, 37, 75)
            with l_horn.Stroke(line_width=4.0) as l_horn_stroker:
                l_horn_stroker.move_to(35, 99)
                l_horn_stroker.quadratic_curve_to(2, 65, 6, 36)
                l_horn_stroker.quadratic_curve_to(17, 60, 37, 75)

    # draw_nostrils Method: This method draws the nostrils and the nose of Tiberius on the canvas.
    def draw_nostrils(self):
        # Draw the nose.
        with self.canvas.Fill(color=rgb(212, 212, 212)) as nose_filler:
            nose_filler.move_to(45, 145)
            nose_filler.bezier_curve_to(51, 123, 96, 123, 102, 145)
            nose_filler.ellipse(73, 114, 39, 47, 0, math.pi / 4, 3 * math.pi / 4)
        # Draw the nostrils.
        with self.canvas.Fill() as nostril_filler:
            nostril_filler.arc(63, 140, 3)  # Draw left nostril
            nostril_filler.arc(83, 140, 3)  # Draw right nostril
        # Draw the nose outline.
        with self.canvas.Stroke(line_width=4.0) as nose_stroker:
            nose_stroker.move_to(45, 145)
            nose_stroker.bezier_curve_to(51, 123, 96, 123, 102, 145)

    # draw_text Method: This method draws the name "Tiberius" below the yak on the canvas.
    def draw_text(self):
        font = toga.Font(family=SANS_SERIF, size=20)
        self.text_width, text_height = self.canvas.measure_text("Tiberius", font)

        x = (150 - self.text_width) // 2  # Center the text horizontally
        y = 175  # Position the text below the yak

        # Draw the border around the text.
        with self.canvas.Stroke(color="REBECCAPURPLE", line_width=4.0) as rect_stroker:
            self.text_border = rect_stroker.rect(
                x - 5,
                y - 5,
                self.text_width + 10,
                text_height + 10,
            )
        # Draw the actual text.
        with self.canvas.Fill(color=rgb(149, 119, 73)) as text_filler:
            self.text = text_filler.write_text("Tiberius", x, y, font, Baseline.TOP)

    # draw_tiberius Method: This method calls the other methods to draw the complete image of Tiberius the yak.
    def draw_tiberius(self):
        self.fill_head()
        self.draw_eyes()
        self.draw_horns()
        self.draw_nostrils()
        self.stroke_head()
        self.draw_text()

    # on_resize Method: This method is called when the canvas is resized.
    # It centers the text horizontally on the canvas.
    def on_resize(self, widget, width, height, **kwargs):
        # Only attempt to reposition the text if there's context objects on the canvas.
        if widget.context:
            left_pad = (width - self.text_width) // 2
            self.text.x = left_pad
            self.text_border.x = left_pad - 5
            widget.redraw()

    # on_press Method: This method is called when the canvas is clicked.
    # It displays a dialog showing the coordinates of the click.
    async def on_press(self, widget, x, y, **kwargs):
        await self.main_window.dialog(
            toga.InfoDialog("Hey!", f"You poked the yak at ({x}, {y})")
        )

# Running the Application
# Entry Point: The main function initializes the StartApp and starts its event loop with main_loop(),
# making the application interactive.
def main():
    # This line initializes the StartApp and returns the application instance.
    return StartApp("Tutorial 4", "org.beeware.toga.tutorial")

if __name__ == "__main__":
    # Start the application event loop.
    main().main_loop()
