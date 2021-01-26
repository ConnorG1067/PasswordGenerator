import tkinter as tk
import random
import paperclip
from tkinter import *
########## Root ##########
root = tk.Tk()
root.title("Pass Gen")
root.geometry('240x200')

########## Variables and Lists ##########
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o' 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', 
'#', '$', '%', '^', '&', '*', '(', ')']

password = " "



def generate():
   
   for i in range(5):
      print(password + random.choice(characters))

passwordTxt = tk.Label(root, bg='#99C8F7', width=35, height=2,)
passwordTxt.grid(row=0, column=0)

Bgenerate = tk.Button(root, text="Generate",width=10, height=1, command=generate)
Bgenerate.grid(row=1, column=0)

passlength = tk.Scale(root, from_=1, to=18, orient=HORIZONTAL)
passlength.grid(row=2, column=0)


root.mainloop()