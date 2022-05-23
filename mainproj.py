from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# widgets
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivymd.uix.taptargetview import MDTapTargetView

# animation/colors
from kivymd.uix.behaviors import MagicBehavior
from kivymd.uix.button import MDFloatingActionButton, MDRoundFlatButton
from kivy.utils import get_color_from_hex

#only for sleep hints:
from Sasha_Brunch.sleep_hints import hints, links
from random import randint
import webbrowser


class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        kv = Builder.load_file('sd1.kv')

        # self.tap_target_view = MDTapTargetView(
        #     widget=kv.ids.test2,
        #     title_text="This is an add button",
        #     description_text="This is a description of the button",
        #     widget_position="left_bottom",
        # )
        return kv


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

# for tests

class TestScreen(Screen):
    pass

class TaskScreen(Screen):

    def set_screen_menu(self):
        MDApp.get_running_app().root.current = "menu"
    def set_screen_task(self):
        MDApp.get_running_app().root.current = "task"
    def set_screen_sleep(self):
        MDApp.get_running_app().root.current = "sleep"


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(NoteScreen(name='note'))
sm.add_widget(SleepScreen(name='sleep'))
sm.add_widget(TaskScreen(name='task'))
sm.add_widget(TestScreen(name='test'))

class WindowManager(ScreenManager):
    pass

# НАРАБОТКИ

class MagicFAB(MagicBehavior, MDFloatingActionButton):
    pass


class OptionScreen(Screen):

    def set_screen_menu(self):
        MDApp.get_running_app().root.current = "menu"


MainApp().run()

#Theme colors
# ['Red', 'Pink', 'Purple', 'DeepPurple',
#  'Indigo', 'Blue', 'LightBlue', 'Cyan',
#  'Teal', 'Green','LightGreen', 'Lime',
#  'Yellow', 'Amber', 'Orange', 'DeepOrange',
#  'Brown', 'Gray', 'BlueGray']


# <TestScreen>:
#
#     ScrollView:
#         do_scroll_x: False
#         do_scroll_y: True
#             Label:
#                 size_hint_y:None
#                 height: self.texture_size[1]
#                 text_size: self.width, None
#                 text: 'test'*1000
#                 font_size: '30sp'

# root.manager.transition.direction = "left"
# root.manager.current = 'task'
