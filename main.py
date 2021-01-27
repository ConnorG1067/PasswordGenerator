import tkinter as tk
import random, string
import pyperclip
from tkinter import *

########## Variables and Lists ##########
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', 
'#', '$', '%', '^', '&', '*', '(', ')']




class application:
   def generate(self):
      self.passw = ""
      for i in range(self.passlength.get()):
         self.passw += random.choice(characters)
      self.passwordTxt["text"] = self.passw

   def copytoclip(self):
      pyperclip.copy(self.passw)

   def __init__(self):
      self.passw = ""
      self.root = tk.Tk()
      self.root.title("Pass Gen")
      self.root.geometry('240x200')
      self.passwordTxt = tk.Label(self.root, bg='#99C8F7', width=35, height=2, text=self.passw)
      self.passwordTxt.grid(row=0, column=0)

      self.Bgenerate = tk.Button(self.root, text="Generate",width=10, height=1, command=self.generate)
      self.Bgenerate.grid(row=1, column=0)

      self.passlength = tk.Scale(self.root, from_=1, to=18, orient=HORIZONTAL)
      self.passlength.grid(row=3, column=0)

      self.copy = tk.Button(self.root, text="Copy", width = 10, height= 1, command=self.copytoclip)
      self.copy.grid(row=2, column=0)

      self.root.mainloop()


application()