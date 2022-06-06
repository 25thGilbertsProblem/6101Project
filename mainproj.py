from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# widgets
from kivy.uix.textinput import TextInput
from kivymd.uix.card import MDCard
from kivy.uix.scrollview import ScrollView
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.picker import MDDatePicker
from datetime import datetime

# animation/colors
from kivy.animation import Animation
from kivymd.uix.behaviors import MagicBehavior
from kivymd.uix.button import MDFloatingActionButton, MDRoundFlatButton
from kivy.utils import get_color_from_hex

# only for sleep hints:
from Sasha_Brunch.sleep_hints import hints, links
from random import randint
import webbrowser


class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = "700"
        kv = Builder.load_file('TheLab.kv')

        # Описание ?-кружочков
        self.tt1 = MDTapTargetView(
            widget=kv.get_screen('menu').idsF.help_1,
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
            target_radius=100,
            title_position="top",
            title_text_size="20sp",

        )

        self.tt3 = MDTapTargetView(
            widget=kv.get_screen('sleep').ids.help_3,
            title_text="        Это кружочек про сон",
            description_text="      Здесь вы получите полезные советы\n      и сможете следить за свои сном",
            widget_position="center",
            outer_radius=450,
            target_radius=80,
            title_position="left_top",
            title_text_size="20sp",

        )

        self.tt4 = MDTapTargetView(
            widget=kv.get_screen('option').ids.help_4,
            title_text="          Это кружочек настроек",
            description_text="      Здесь вы можете поменять цвет кружочков\n               и включить темную тему",
            widget_position="center",
            outer_radius=450,
            target_radius=80,
            title_position="left_top",
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

    def tt3_start(self):
        if self.tt3.state == "close":
            self.tt3.start()

        else:
            self.tt3.stop()

    def tt4_start(self):
        if self.tt4.state == "close":
            self.tt4.start()

        else:
            self.tt4.stop()

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
        text = TextInput(text='')
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
    pic = 'images/' + str(i) + '.jpeg'

    def prove(instance):
        open_link()


# for tests

class TestScreen(Screen):
    def set_screen_menu(self):
        MDApp.get_running_app().root.current = "menu"

    def on_enter(self):
        for i in range(10):
            self.manager.get_screen('test').ids.test_id.add_widget()

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


#######
class TaskScreen(Screen):

    def set_screen_menu(self):
        MDApp.get_running_app().root.current = "menu"

    def set_screen_note(self):
        MDApp.get_running_app().root.current = "note"

    def set_screen_sleep(self):
        MDApp.get_running_app().root.current = "sleep"

    task_list_dialog = None

    def show_task_dialog(self):
        if not self.task_list_dialog:
            dialog_context = DialogContent()
            self.task_list_dialog = MDDialog(
                title="Создайте напоминание",
                type="custom",
                content_cls=dialog_context,
            )
            dialog_context.set_parent_widget(self)

        self.task_list_dialog.open()


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(NoteScreen(name='note'))
sm.add_widget(SleepScreen(name='sleep'))
sm.add_widget(TaskScreen(name='task'))
sm.add_widget(TestScreen(name='test'))


class WindowManager(ScreenManager):
    pass


# НАРАБОТКИ

class DialogContent(MDBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = str(datetime.now().strftime('%A %d %B %Y'))

    def set_parent_widget(self, widget):
        self.parent_widget = widget

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        date = value.strftime('%A %d %B %Y')
        self.ids.date_text.text = str(date)

    def add_task(self, task, task_date):
        print(task.text, task_date)
        self.parent_widget.ids['container'].add_widget(ListItemWithCheckbox(text='[b]' + task.text + '[/b]', secondary_text=task_date))
        task.text = ''

    def close_dialog(self, *args):
        self.parent_widget.task_list_dialog.dismiss()



class MagicFAB(MagicBehavior, MDFloatingActionButton):
    pass



class OptionScreen(Screen):

    def set_screen_menu(self):
        MDApp.get_running_app().root.current = "menu"

class ListItemWithCheckbox(TwoLineAvatarIconListItem):

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk


    def mark(self, check, the_list_item):
        if check.active == True:
            the_list_item.text = '[s]'+the_list_item.text+'[/s]'
        else:

            pass

    def delete_item(self, the_list_item):
        '''Delete the task'''
        self.parent.remove_widget(the_list_item)

class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    '''Custom left container'''

MainApp().run()

# Theme colors
# ['Red', 'Pink', 'Purple', 'DeepPurple',
#  'Indigo', 'Blue', 'LightBlue', 'Cyan',
#  'Teal', 'Green','LightGreen', 'Lime',
#  'Yellow', 'Amber', 'Orange', 'DeepOrange',
#  'Brown', 'Gray', 'BlueGray']


# root.manager.transition.direction = "left"
# root.manager.current = 'task'

# overlay_color: app.overlay_color[:-1] + [.2]
#                 icon_bg_color: app.overlay_color
#                 on_selected: app.on_selected(*args)
#                 on_unselected: app.on_unselected(*args)
#                 on_selected_mode: app.set_selection_mode(*args)
