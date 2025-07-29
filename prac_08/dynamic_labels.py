from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App to display dynamic labels for a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # List of names to display
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        """Build the Kivy UI and add Labels dynamically."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create and add Label widgets for each name."""
        for name in self.names:
            label = Label(text=name, font_size=24)
            self.root.ids.main.add_widget(label)


if __name__ == '__main__':
    DynamicLabelsApp().run()

