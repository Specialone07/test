from typing import Self
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.text
a = int(input("enter any number"))
b = int(input("enter any number"))
Self.window.add_widget(Image(Self("logo_image.png")))
if(a>b):
    print("code is executed")
print("Adding Two Numbers:", a + b)
print("Subtraction of Two Numbers:", a - b)
print("Multiplication of Two Numbers:", a * b)
print("Division of Two Numbers:", a / b)
print("Modulus of Two Numbers:", a % b)
print("Floor Division Of Two Numbers:", a // b)
