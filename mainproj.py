from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"



        return Builder.load_file('TheLab.kv')

class MenuScreen(Screen):
    pass

class NoteScreen(Screen):
    pass

class SleepScreen(Screen):
    pass

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
