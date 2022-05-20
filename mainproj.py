from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
from kivymd.uix.picker import MDTimePicker

#only for sleep hints:
from Sasha_Brunch.sleep_hints import hints, links
from random import randint
import webbrowser


class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        def show_time_picker(self):
            time_dialog = MDTimePicker()
            time_dialog.open()



        return Builder.load_file('sd1.kv')

class MenuScreen(Screen):
    pass

class NoteScreen(Screen):

    def set_screen_menu(self):
        MDApp.get_running_app().root.current = "menu"
    def set_screen_task(self):
        MDApp.get_running_app().root.current = "task"
    def set_screen_sleep(self):
        MDApp.get_running_app().root.current = "sleep"
    def add_test(self):
        text = TextInput(text = '')
        self.ids.note_id.add_widget(text)

########
# Sleep

i = randint(0, 8)


def open_link():
    global i
    webbrowser.open(links[i])
    return i
#########

class SleepScreen(Screen):

    def set_screen_menu(self):
        MDApp.get_running_app().root.current = "menu"
    def set_screen_note(self):
        MDApp.get_running_app().root.current = "note"
    def set_screen_task(self):
        MDApp.get_running_app().root.current = "task"


    #########
    hint = hints[i]

    def prove(instance):
        open_link()

class TaskScreen(Screen):

    def set_screen_menu(self):
        MDApp.get_running_app().root.current = "menu"
    def set_screen_task(self):
        MDApp.get_running_app().root.current = "task"
    def set_screen_sleep(self):
        MDApp.get_running_app().root.current = "sleep"

class OptionScreen(Screen):

    def set_screen_menu(self):
        MDApp.get_running_app().root.current = "menu"

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(NoteScreen(name='note'))
sm.add_widget(SleepScreen(name='sleep'))
sm.add_widget(TaskScreen(name='task'))

class WindowManager(ScreenManager):
    pass

MainApp().run()

#Theme colors
# ['Red', 'Pink', 'Purple', 'DeepPurple',
#  'Indigo', 'Blue', 'LightBlue', 'Cyan',
#  'Teal', 'Green','LightGreen', 'Lime',
#  'Yellow', 'Amber', 'Orange', 'DeepOrange',
#  'Brown', 'Gray', 'BlueGray']


# MDLabel:
# text: "1 test"
# halign: 'center'
# MDLabel:
# text: "2 test"
# halign: 'center'
# MDLabel:
# text: "3 test"
# halign: 'center'
#
# MDBottomAppBar:
# MDToolbar:
# elevation: 0
# mode: 'end'
# type: 'bottom'
# icon: 'plus'
# icon_color: .7, .2, .1,
# left_action_items:
# [["arrow-left", lambda x: root.set_screen_menu()],
#  ["check-bold", lambda x: root.set_screen_task()],
#  ["sleep", lambda x: root.set_screen_sleep()]]
#
# on_action_button: root.add_test()
