import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix import label


class BoxLayoutExample(BoxLayout):
    pass 

#     def __init__(self, **kwargs):
#         super(BoxLayoutExample, self).__init__(**kwargs)
#         self.orientation = "vertical"  # ---> "horizontal"
#         b1 = Button(text="Button 1")
#         b2 = Button(text="Button 2")
#         b3 = Button(text="Button 3")
#         self.add_widget(b1)
#         self.add_widget(b2)
#         self.add_widget(b3)

# class BoxLayoutApp(App):               # dont need when we give kv language
#     def build(self):   
#         return BoxLayoutExample()
     

class BoxLayoutApp(App):  #Need when 
    pass
    
if __name__ == "__main__":
    BoxLayoutApp().run()