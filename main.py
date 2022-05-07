from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from random import randint
import webbrowser
from sleep_hints import links, hints

Window.size = (540, 1000)
class MyApp(App):
    def build(self):
        layout = FloatLayout(size=(540, 1000))

        def callback_sleep(instance):
            # delete main menu
            layout.remove_widget(goalbtn)
            layout.remove_widget(sleepbtn)
            layout.remove_widget(taskbtn)
            layout.remove_widget(sleep)
            layout.remove_widget(tasks)
            layout.remove_widget(goal)

            # Controls which hint and link to the research will be shown
            i = randint(0, 8)
            random_hint = str(hints[i])

            def open_link(instance1):
                webbrowser.open(links[i])

            # create sleep menu

            hint = Label(text="Советы по улучшению сна:"
                              "", font_size='25sp', pos=(0, 400))

            link = Button(text=random_hint,
                          font_size='20sp', size_hint=(.7, .2), pos=(80, 600),
                          background_color=(0, 0, 0, 0),
                          on_press=open_link, border='5p')
            Textfeeld = TextInput(text='00:00', multiline=True, size_hint=(0.6, 0.1), pos=(100, 40), font_size=25, background_color=(0.4, 0.3, 1, 1))

            def main_menu(instance):
                layout.remove_widget(hint)
                layout.remove_widget(link)
                layout.remove_widget(back_button)
                layout.remove_widget(back_button_logo)
                layout.remove_widget(Textfeeld)

                layout.add_widget(goalbtn)
                layout.add_widget(sleepbtn)
                layout.add_widget(taskbtn)
                layout.add_widget(sleep)
                layout.add_widget(tasks)
                layout.add_widget(goal)
                return goalbtn, sleepbtn, taskbtn, sleep, tasks, goal

            back_button = Button(size_hint=(.1, .05), pos=(10, 830), on_press=main_menu, background_color=(0, 0, 0, 0))
            back_button_logo = Image(source='additional/left.png', size_hint=(.3, .15), pos=(-35, 787))

            layout.add_widget(hint)
            layout.add_widget(link)
            layout.add_widget(back_button)
            layout.add_widget(back_button_logo)
            layout.add_widget(Textfeeld)

        sleepbtn = Button(size_hint=(.30, .135), pos=(80, 550), background_color=(0, 0, 0, 0), on_press=callback_sleep)
        goalbtn = Button(size_hint=(.30, .135), pos=(70, 300), background_color=(0, 0, 0, 0))
        taskbtn = Button(size_hint=(.30, .135), pos=(275, 400), background_color=(0, 0, 0, 0))
        wallper = Image(source='additional/wallper1.png', size_hint=(2, 1), pos=(-40, 0))
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



