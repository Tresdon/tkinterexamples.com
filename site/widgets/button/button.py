# Simple
import tkinter
from tkinter import messagebox

def show_alert():
    messagebox.showinfo("Window Title", "Hello world!")

root = tkinter.Tk()
root.title("tkinterexamples.com")

tkinter.Button(root, text="Click Me", command=show_alert).pack()

root.mainloop()


# Button with image
from PIL import Image, ImageTk
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title("tkinterexamples.com")

image_tk = ImageTk.PhotoImage(Image.open("/Users/tresdon/Downloads/save.png").resize((100,100))) 

tkinter.Button(root, image=image_tk).pack()

root.mainloop()


# Disabled
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

button = tkinter.Button(root, text="Click Me", state=tkinter.DISABLED)
button.pack()

button["command"] = lambda: print("HELLO WORLD!")
button["state"] = tkinter.NORMAL

root.mainloop()