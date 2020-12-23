import tkinter
from tkinter import *

def main():
   o=[]
   b=a.get()
   s = [char for char in b]
   for i in range(len(s)):
       if 1072<=ord(s[i])<=1103:
           o.append(chr(1072 + (1103 - ord(s[i]))))
       elif 1040<=ord(s[i])<=1071:
           o.append(chr(1040 + (1071 - ord(s[i]))))
       else:
           o.append(s[i])
   g=''.join(map(str, o))
   return a.set(g)

window = Tk()
window.title("Шифр Атбаш")
window.geometry('270x100')
a =StringVar()
pole = Entry(window,width=40 ,textvariable=a)
pole.place(x=,y=10)
knopka = tkinter.Button(window, text = "Зашифровать",command = main)
knopka.place(x=85,y=50)
window.mainloop()