import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class interface(Widget):
    def logicfn(self):
        print("text entered")

class Test2App(App):
    pass

if __name__ == "__main__":
    Test2App().run()