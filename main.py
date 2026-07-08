from kivy.app import App
from kivy.lang import Builder

KV = """
BoxLayout:
    orientation: "vertical"
    padding: 10
    spacing: 10

    TextInput:
        id: display
        text: "0"
        font_size: 42
        readonly: True
        halign: "right"
        multiline: False
        size_hint_y: 0.2

    GridLayout:
        cols: 4
        spacing: 5

        Button:
            text: "7"
            on_press: app.add("7")
        Button:
            text: "8"
            on_press: app.add("8")
        Button:
            text: "9"
            on_press: app.add("9")
        Button:
            text: "/"
            on_press: app.add("/")

        Button:
            text: "4"
            on_press: app.add("4")
        Button:
            text: "5"
            on_press: app.add("5")
        Button:
            text: "6"
            on_press: app.add("6")
        Button:
            text: "*"
            on_press: app.add("*")

        Button:
            text: "1"
            on_press: app.add("1")
        Button:
            text: "2"
            on_press: app.add("2")
        Button:
            text: "3"
            on_press: app.add("3")
        Button:
            text: "-"
            on_press: app.add("-")

        Button:
            text: "C"
            on_press: app.clear()

        Button:
            text: "0"
            on_press: app.add("0")

        Button:
            text: "="
            on_press: app.calc()

        Button:
            text: "+"
            on_press: app.add("+")
"""

class Calculator(App):
    def build(self):
        self.exp = ""
        return Builder.load_string(KV)

    def add(self, value):
        if self.exp == "Error":
            self.exp = ""
        self.exp += value
        self.root.ids.display.text = self.exp

    def clear(self):
        self.exp = ""
        self.root.ids.display.text = "0"

    def calc(self):
        try:
            self.exp = str(eval(self.exp))
        except:
            self.exp = "Error"
        self.root.ids.display.text = self.exp

Calculator().run()
