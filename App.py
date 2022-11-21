from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Mygridlayout(GridLayout):
    def __init__(self, **kwargs):
        #Calling the grid layoit constructor
        super(Mygridlayout, self).__init__(**kwargs)

        #main grid
        #Set columns
        self.cols = 1

        #subgrid 1
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        #Add name widget
        self.age_label = Label(text = "Age :")
        self.name_label = Label(text = "NAme :")
        self.num_label = Label(text = "NUmber :")
        #Add Input text box
        self.name = TextInput(multiline=False, 
                size_hint_y = None,
                height = 50,
                size_hint_x=None,
                width=400)
        self.age = TextInput(multiline=False,size_hint_y = None,
                height = 50,
                size_hint_x=None,
                width=400)
        self.num = TextInput(multiline=False,size_hint_y = None,
                height = 50,
                size_hint_x=None,
                width=400) 
        
        #first instance 
        self.top_grid.add_widget(self.name_label)
        self.top_grid.add_widget(self.name)

        #secotop_grid.nd instance
        self.top_grid.add_widget(self.age_label)
        self.top_grid.add_widget(self.age)

        #thirtop_grid.d instance
        self.top_grid.add_widget(self.num_label)
        self.top_grid.add_widget(self.num)

        #adding top widgets to minn gris
        self.add_widget(self.top_grid)

        #submit button
        self.submit = Button(text="Press", font_size=32,size_hint_y = None,
                height = 50,
                size_hint_x=None,
                width=400)
        #bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
        
    def press(self, instance):
        name = self.name.text
        age = self.age.text
        num = self.num.text

        self.name.text = ""
        self.age.text =  ""
        self.num.text = ""

        self.add_widget(Label(text=f"hi {name} and your age is {age} and num {num}"))



        




class MyApp(App):
    def build(self):
        return Mygridlayout()

if __name__ == '__main__':
    MyApp().run()