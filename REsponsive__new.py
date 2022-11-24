from kivy.app import App
from kivy.lang import Builder
from kivy.properties import OptionProperty
from kivy.core.window import Window
from kivy.factory import Factory


class ResponsiveNewApp(App):
    media = OptionProperty('M', options=('XS', 'SmartPhone', 'Tablet','Laptop', 'Desktop'))

    def build(self):
        Window.bind(size=self.update_media)
        # return Builder.load_file("ResponsiveNew.kv")

    def update_media(self, win, size):
        width, height = size
        self.media = (
            'XS' if width < 320 else
            'SmartPhone' if width < 768 else
            'Tablet' if width < 1024 else
            'Laptop' if width < 1680 else
            'Desktop'
        )

if __name__ == "__main__":
    ResponsiveNewApp().run()