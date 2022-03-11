from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class MainWindow(Screen):
    def sleep_on(self):
        self.ids.sleep_image.source = 'sleep_turn+.png'
    def sleep_off(self):
        self.ids.sleep_image.source = 'sleep.png'
    def tasks_on(self):
        self.ids.tasks_image.source = 'task_turn+.png'
    def tasks_off(self):
        self.ids.tasks_image.source = 'tasks.png'
        self.root_window = MondayWindow
    def goal_on(self):
        self.ids.goal_image.source = 'goal_turn+.png'
    def goal_off(self):
        self.ids.goal_image.source = 'goal.png'





  class MondayWindow(Screen):
    pass

class TuesdayWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class App(App):
    def build(self):
        return kv


kv = Builder.load_file("TheLab.kv")
if __name__ == "__main__":
    App().run()