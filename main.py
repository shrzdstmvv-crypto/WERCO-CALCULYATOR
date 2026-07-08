from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        self.a = TextInput(hint_text="1-son", multiline=False, input_filter="float")
        self.b = TextInput(hint_text="2-son", multiline=False, input_filter="float")

        self.add_widget(self.a)
        self.add_widget(self.b)

        btn = Button(text="Hisobla")
        btn.bind(on_press=self.calculate)
        self.add_widget(btn)

        self.result = Label(text="Natija: 0")
        self.add_widget(self.result)

    def calculate(self, instance):
        try:
            x = float(self.a.text)
            y = float(self.b.text)
            self.result.text = f"Natija: {x + y}"
        except:
            self.result.text = "Xatolik!"


class WercoCalculator(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    WercoCalculator().run()
