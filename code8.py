import kivy
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.scrollview import ScrollView

class Interface(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # b1 = Button(text="Button 1", size_hint=(0.15,0.15))
        # b2 = Button(text="Button 2", size_hint=(0.15,0.15))
        # self.add_widget(b1)
        # self.add_widget(b2)
        for i in range(200):
            button = Button(text=f"Button {i+1}", size_hint= (None,None), size=(100,100))
            self.add_widget(button)

class Scrollerfn():
    pass 

class LLmApp(App):
    pass

if __name__ == "__main__":
    LLmApp().run()