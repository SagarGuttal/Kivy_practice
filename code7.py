import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class ManinScreen(FloatLayout):
    sideLayout = BoxLayout(size_hint=(0.5,0.5))
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Button 1", size_hint=(0.2,0.2))
        self.sideLayout.add_widget(b1)
        self.add_widget(self.sideLayout)


class FloatLayoutExampleApp(App):
    pass

if __name__ == "__main__":
    FloatLayoutExampleApp().run()