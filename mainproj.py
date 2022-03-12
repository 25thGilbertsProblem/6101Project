from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Основное окно виджетов <статично>
class MainWindow(Screen):
    def sleep_on(self):
        self.ids.sleep_image.source = 'images/sleep_turn+.png'
    def sleep_off(self):
        self.ids.sleep_image.source = 'images/sleep.png'
    def tasks_on(self):
        self.ids.tasks_image.source = 'images/task_turn+.png'
    def tasks_off(self):
        self.ids.tasks_image.source = 'images/task.png'
        self.root_window = MondayWindow
    def goal_on(self):
        self.ids.goal_image.source = 'images/goal_turn+.png'
    def goal_off(self):
        self.ids.goal_image.source = 'images/goal.png'
    def red_on(self):
        self.ids.bip_red_image.source = 'images/bip_red.png'
    def red_off(self):
        self.ids.bip_red_image.source = 'images/bip_red.png'
    def yellow_on(self):
        self.ids.bip_yellow_image.source = 'images/bip_yellow.png'
    def yellow_off(self):
        self.ids.bip_yellow_image.source = 'images/bip_yellow.png'
    def green_on(self):
        self.ids.bip_green_image.source = 'images/bip_green.png'
    def green_off(self):
        self.ids.bip_green_image.source = 'images/bip_green.png'





class MondayWindow(Screen):
    pass

class TuesdayWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

# Приложение, запускает kv файл
class TheApp(App):
    def build(self):
        return kv


class RootWidget(FloatLayout):
    pass

class ImButton(ButtonBehavior, Image):
    def on_press(self):
        print ('pr')


kv = Builder.load_file("TheLab.kv")


if __name__ == "__main__":
    TheApp().run()