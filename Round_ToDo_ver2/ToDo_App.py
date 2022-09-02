#main imports
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.properties import NumericProperty


#uix
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.snackbar import Snackbar

import datetime
from datetime import date

#fixed window sizes
Window.size = (350, 650)

class ToDo_App(MDApp):

    def build(self):

        # theme style
        # self.theme_cls.theme_style = ""

        global screen_manager
        screen_manager = ScreenManager()
        # priority of screens:

        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("AddTodo.kv"))
        screen_manager.add_widget(Builder.load_file("Matrix.kv"))
        return screen_manager

    def on_start(self):
        #initialize time
        today = date.today()
        wd = date.weekday(today)
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().strftime("%b"))
        day = str(datetime.datetime.now().strftime("%d"))
        screen_manager.get_screen("main").date.text = f"{days[wd]}, {day}, {month}, {year}"


    def on_complete(self, checkbox, value, description, bar):
        if value:
            description.text = f"[s]{description.text}[/s]"
            bar.md_bg_color = 0, 179/255, 0, 1
        else:
            remove = ["[s]","[/s]"]
            for i in remove:
                description.text = description.text.replace(i, "")
                bar.md_bg_color = 1, 170/255, 23/255, 1

    def add_card(self, title, description, back_color):
        if title != "":
            screen_manager.get_screen("main").todo_list.add_widget(ToDo_Card(title = title, description = description, back_color = back_color))
            screen_manager.get_screen("add_todo").description.text = ""
            screen_manager.get_screen("add_todo").title.text = ""

            Snackbar(text="Добавлено",
                     snackbar_x="5dp", snackbar_y="10dp",
                     size_hint_y=.08,
                     size_hint_x=(Window.width - (10 * 2)) / Window.width,
                     bg_color=(1, 170 / 255, 23 / 255, 1),
                     font_size="18sp",
                     duration = 0.2).open()

        elif title == "":
            Snackbar(text= "Нет названия",
                     snackbar_x = "5dp", snackbar_y = "10dp",
                     size_hint_y = .08,
                     size_hint_x = (Window.width-(10 * 2)) /Window.width,
                     bg_color= (1, 170/255, 23/255, 1),
                     font_size = "18sp",
                     duration = 0.2).open()

    def remove_card(self, card):
        screen_manager.get_screen("main").todo_list.remove_widget(card)
        pass

    #choose the color of card back (dep from usr rating)
    def choose_color(self, n):
        # initialize colors
        col = [[1, 1, 1, 1], [1, 215/255, 145/255, 1], [1, 200/255, 105/255, 1], [1, 170/255, 23/255, 1], [207/255, 38/255, 0, 0.8],]
        color = col[n]
        print(f'{n} and {color}')
        return color


# cards structure
class ToDo_Card(FakeRectangularElevationBehavior, MDFloatLayout):
    title = StringProperty()
    description = StringProperty()
    back_color = NumericProperty()




if __name__ == '__main__':
    ToDo_App().run()