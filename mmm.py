from kivy.app import App
from kivy.uix.button import Button
from kivy.modules import keybinding
from kivy.core.window import Window

class Demo(App):

    def build(self):
        button = Button(text="Hello")
        keybinding.start(Window, button)
        return button

if __name__ == "__main__":
    Demo().run()