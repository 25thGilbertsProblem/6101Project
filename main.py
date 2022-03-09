from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from random import randint
from kivy.uix.label import Label
import webbrowser
from sleep_hints import links, hints

Window.size = (450, 900)


class MyApp(App):
    def build(self):
        layout = FloatLayout(size=(450, 900))

        def callback_sleep(instance):
            # delete main menu
            layout.remove_widget(goalbtn)
            layout.remove_widget(sleepbtn)
            layout.remove_widget(taskbtn)
            layout.remove_widget(goal)
            layout.remove_widget(tasks)
            layout.remove_widget(sleep)

            # create sleep menu
            i = randint(0, 2)

            def open_link(instance1):
                webbrowser.open(links[i])

            hint = Label(text="Советы по улучшению сна:", font_size='25sp', pos=(0, 400))

            link = Button(
                text='Короткий сон приводит к \nповышенной смертности, \n возникновению диабета, \nпроблемам с сердечнососудистой \nсистемой, ишемической болезни сердца,\n ожирению. Идеальное время сна\n - 7-8 часов.',
                font_size='20sp', size_hint=(.7, .2), pos=(80, 600),
                background_color=(0, 0, 0, 0),
                on_press=open_link, border='5p')

            def main_menu(instance):
                layout.remove_widget(hint)
                layout.remove_widget(link)
                layout.remove_widget(back_button)
                layout.remove_widget(back_button_logo)

                sleepbtn = Button(size_hint=(.30, .135), pos=(80, 550), background_color=(0, 0, 0, 0),
                                  on_press=callback_sleep)
                goalbtn = Button(size_hint=(.30, .135), pos=(70, 300), background_color=(0, 0, 0, 0))
                taskbtn = Button(size_hint=(.30, .135), pos=(275, 400), background_color=(0, 0, 0, 0))
                wallper = Image(source='additional/wallper1.png', size_hint=(2, 1))
                sleep = Image(source='additional/sleep.png', size_hint=(.5, .25), pos=(35, 500))
                tasks = Image(source='additional/tasks.png', size_hint=(.5, .25), pos=(230, 350))
                goal = Image(source='additional/goal.png', size_hint=(.5, .25), pos=(25, 250))

                layout.add_widget(wallper)
                layout.add_widget(goalbtn)
                layout.add_widget(sleepbtn)
                layout.add_widget(taskbtn)
                layout.add_widget(sleep)
                layout.add_widget(tasks)
                layout.add_widget(goal)

            back_button = Button(size_hint=(.1, .05), pos =(100, 100), on_press=main_menu)
            back_button_logo = Image(source='additional/left.png', size_hint=(.2, .1), pos=(76, 78))

            layout.add_widget(hint)
            layout.add_widget(link)
            layout.add_widget(back_button)
            layout.add_widget(back_button_logo)

        sleepbtn = Button(size_hint=(.30, .135), pos=(80, 550), background_color=(0, 0, 0, 0), on_press=callback_sleep)
        goalbtn = Button(size_hint=(.30, .135), pos=(70, 300), background_color=(0, 0, 0, 0))
        taskbtn = Button(size_hint=(.30, .135), pos=(275, 400), background_color=(0, 0, 0, 0))
        wallper = Image(source='additional/wallper1.png', size_hint=(2, 1))
        sleep = Image(source='additional/sleep.png', size_hint=(.5, .25), pos=(35, 500))
        tasks = Image(source='additional/tasks.png', size_hint=(.5, .25), pos=(230, 350))
        goal = Image(source='additional/goal.png', size_hint=(.5, .25), pos=(25, 250))

        layout.add_widget(wallper)
        layout.add_widget(goalbtn)
        layout.add_widget(sleepbtn)
        layout.add_widget(taskbtn)
        layout.add_widget(sleep)
        layout.add_widget(tasks)
        layout.add_widget(goal)
        return layout


if __name__ == "__main__":
    MyApp().run()
