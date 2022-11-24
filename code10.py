from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Page_layout(PageLayout):
    pass

# class Page_1(BoxLayout):             
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         b1 = Button(text= "p1-b1")
#         b2 = Button(text="p2-b2")
#         self.add_widget(b1)
#         self.add_widget(b2)

# class Page_2(BoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         b1 = Button(text= "p2-b1")
#         b2 = Button(text="p2-b2")
#         self.add_widget(b1)
#         self.add_widget(b2)

# class Page_3(BoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         b1 = Button(text="p3-b1")
#         b2 = Button(text="p3-b2")
#         self.add_widget(b1)
#         self.add_widget(b2)

class PageLayoutExampleApp(App):
    pass

if __name__ == "__main__":
    PageLayoutExampleApp().run()