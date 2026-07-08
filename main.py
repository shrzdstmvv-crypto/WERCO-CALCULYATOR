from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calc(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(cols=4, padding=8, spacing=8, **kwargs)
        self.expr=""
        self.display=TextInput(readonly=True,multiline=False,font_size=40,halign="right")
        self.add_widget(self.display)
        for _ in range(3):
            self.add_widget(Button(disabled=True,opacity=0))
        for t in ["C","⌫","%","/","7","8","9","*","4","5","6","-","1","2","3","+","0",".","=",""]:
            if t=="":
                self.add_widget(Button(disabled=True,opacity=0)); continue
            b=Button(text=t,font_size=28)
            b.bind(on_press=self.press)
            self.add_widget(b)
    def press(self,btn):
        t=btn.text
        if t=="C": self.expr=""
        elif t=="⌫": self.expr=self.expr[:-1]
        elif t=="=":
            try:self.expr=str(eval(self.expr))
            except:self.expr="Error"
        elif t=="%":
            try:self.expr=str(float(self.expr)/100)
            except:self.expr="Error"
        else:
            if self.expr=="Error": self.expr=""
            self.expr+=t
        self.display.text=self.expr

class WercoCalculator(App):
    def build(self): return Calc()

WercoCalculator().run()
