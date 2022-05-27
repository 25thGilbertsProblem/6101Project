from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# widgets
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.uix.list import TwoLineAvatarListItem
from kivymd.uix.list import OneLineListItem


# animation/colors
from kivy.animation import Animation
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
        self.theme_cls.primary_hue = "700"
        kv = Builder.load_file('sd1.kv')

        #Описание ?-кружочков
        self.tt1 = MDTapTargetView(
            widget=kv.get_screen('menu').ids.help_1,
            title_text="Это основное меню",
            description_text="Здесь распологаются \n кружочки-виджеты",
            widget_position="left_bottom",
            title_text_size="20sp",

        )
        self.tt2 = MDTapTargetView(
            widget=kv.get_screen('menu').ids.help_2,
            title_text="Это кнопка \n добавления",
            description_text="Добавьте что-то новое \n в кружочек)",
            description_text_color=[0, 0, 0, 1],
            title_text_color=[0, 0, 0, 1],
            outer_circle_color=(1, 1, 1,),
            widget_position="center",
            target_circle_color=(1, 1, 1),
            target_radius = 100,
            title_position="top",
            title_text_size="20sp",

        )

        return kv

    def tt1_start(self):
        if self.tt1.state == "close":
            self.tt1.start()

        else:
            self.tt1.stop()

    def tt2_start(self):
        if self.tt2.state == "close":
            self.tt2.start()

        else:
            self.tt2.stop()
    overlay_color = get_color_from_hex("#6042e4")

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
    def set_screen_menu(self):
        MDApp.get_running_app().root.current = "menu"

    def on_enter(self):
        for i in range(10):
            self.manager.get_screen('test').ids.test_id.add_widget(MyItem())
    def set_selection_mode(self, instance_selection_list, mode):
        if mode:
            md_bg_color = self.overlay_color
            left_action_items = [
                [
                    "close",
                    lambda x: self.root.ids.selection_list.unselected_all(),
                ]
            ]
            right_action_items = [["trash-can"], ["dots-vertical"]]
        else:
            md_bg_color = (0, 0, 0, 1)
            left_action_items = [["menu"]]
            right_action_items = [["magnify"], ["dots-vertical"]]
            self.manager.get_screen('test').ids.toolbar.title = "Inbox"

        Animation(md_bg_color=md_bg_color, d=0.2).start(self.root.ids.toolbar)
        self.manager.get_screen('test').ids.toolbar.left_action_items = left_action_items
        self.manager.get_screen('test').ids.toolbar.right_action_items = right_action_items

    def on_selected(self, instance_selection_list, instance_selection_item):
        self.manager.get_screen('test').ids.toolbar.title = str(
            len(instance_selection_list.get_selected_list_items())
        )

    def on_unselected(self, instance_selection_list, instance_selection_item):
        if instance_selection_list.get_selected_list_items():
            self.manager.get_screen('test').ids.toolbar.title = str(
                len(instance_selection_list.get_selected_list_items())
            )


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

class MyItem(TwoLineAvatarListItem):
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

# root.manager.transition.direction = "left"

# overlay_color: app.overlay_color[:-1] + [.2]
#                 icon_bg_color: app.overlay_color
#                 on_selected: app.on_selected(*args)
#                 on_unselected: app.on_unselected(*args)
#                 on_selected_mode: app.set_selection_mode(*args)
