from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class CommonComponentLabel(MDLabel):
    pass


class MobileView(MDScreen):
    pass



class TabletView(MDScreen):
    pass

    
class DesktopView(FloatLayout):
    pass


class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()
        

    def on_rotate(self):
        self.screen.canvas.ask_update()

class responsiveApp(MDApp):
    pass

if __name__ == "__main__":
    responsiveApp().run()