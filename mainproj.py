from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

#only for sleep hints:
from Sasha_Brunch.sleep_hints import hints, links
from random import randint
import webbrowser


class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"



        return Builder.load_file('TheLab.kv')

class MenuScreen(Screen):
    pass

class NoteScreen(Screen):
    pass

########
# Sleep

i = randint(0, 8)


def open_link():
    global i
    webbrowser.open(links[i])
    return i
#########

class SleepScreen(Screen):
    hint = hints[i]

    def prove(instance):
        open_link()

class TaskScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(NoteScreen(name='note'))
sm.add_widget(SleepScreen(name='sleep'))
sm.add_widget(TaskScreen(name='task'))

class WindowManager(ScreenManager):
    pass


MainApp().run()
