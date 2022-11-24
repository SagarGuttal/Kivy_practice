from kivy.app import App
from kivy.lang import Builder
from kivy.properties import OptionProperty
from kivy.core.window import Window
from kivy.factory import Factory



class NewResponsiveApp(App):
    media = OptionProperty('M', options=('XS', 'S', 'M', 'L', 'XL'))

    # def build(self):
    #     Window.bind(size=self.update_media)
    #     return Builder.load_string(KV)

    def update_media(self, win, size):
        width, height = size
        self.media = (
            'XS' if width < 250 else
            'S' if width < 500 else
            'M' if width < 1000 else
            'L' if width < 1200 else
            'XL'
        )

if __name__ == "__main__":
    NewResponsiveApp().run()