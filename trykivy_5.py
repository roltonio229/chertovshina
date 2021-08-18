# программа с двумя экранами
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
# Экран (объект класса Screen) - это виджет типа "макет" (Screen - наследник класса RelativeLayout).
#800 600 ScreenManager - это особый виджет, который делает видимым один из прописанных в нём экранов.

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        i = Image(source="start.jpg")
        self.add_widget(i)
        btn = Button(text="вправо",size_hint=(None,None))
        btn.on_press = self.next
        btn.size = (50,150)
        btn.pos = (0,250)
        self.add_widget(btn)
        btn1 = Button(text="влево",size_hint=(None,None))
        btn1.on_press = self.next1
        btn1.size = (50,150)
        btn1.pos = (750,250)
        self.add_widget(btn1)
        btn2 = Button(text="вниз",size_hint=(None,None))
        btn2.on_press = self.next2
        btn2.size = (150,50)
        btn2.pos = (325,0)
        self.add_widget(btn2)
        btn3 = Button(text="вверх",size_hint=(None,None))
        btn3.on_press = self.next3
        btn3.size = (150,50)
        btn3.pos = (325,550)
        self.add_widget(btn3)

    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'second'
    def next1(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'theard'
    def next2(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'fourth'
    def next3(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'fifth'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text="Вернись, вернись!")
        btn.on_press = self.next
        self.add_widget(btn)
        
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'

class TheardScr(Screen):
    def __init__(self, name='theard'):
        super().__init__(name=name)
        btn = Button(text="Верь!")
        btn.on_press = self.next
        self.add_widget(btn)
        
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class FourthScr(Screen):
    def __init__(self, name='fourth'):
        super().__init__(name=name)
        btn = Button(text="Вернись!")
        btn.on_press = self.next
        self.add_widget(btn)
        
    def next(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'first'

class FifthScr(Screen):
    def __init__(self, name='fifth'):
        super().__init__(name=name)
        btn = Button(text="рататуй!")
        btn.on_press = self.next
        self.add_widget(btn)
        
    def next(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(TheardScr())
        sm.add_widget(FourthScr())
        sm.add_widget(FifthScr())
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        return sm

app = MyApp()
app.run()