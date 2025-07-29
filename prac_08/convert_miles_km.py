from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

CONVERSION_FACTOR = 1.60934


class MilesToKmConverterApp(App):
    output_text = StringProperty()  # This will be bound to the output label

    def build(self):
        Window.size = (400, 200)
        self.title = "Miles to Kilometres Converter"
        self.output_text = "0.0 km"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_conversion(self, value):
        """Convert miles to km and update label."""
        try:
            miles = float(value)
            km = miles * CONVERSION_FACTOR
            self.output_text = f"{km:.3f} km"
        except ValueError:
            self.output_text = "0.0 km"

    def handle_increment(self, text_value, change):
        """Increase or decrease the miles value."""
        try:
            current = int(text_value)
        except ValueError:
            current = 0
        new_value = current + change
        self.root.ids.input_miles.text = str(new_value)
        self.handle_conversion(new_value)


if __name__ == "__main__":
    MilesToKmConverterApp().run()
