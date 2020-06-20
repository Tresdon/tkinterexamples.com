# General
import tkinter

root = tkinter.Tk()

def key_handler(event):
    print(event.char, event.keysym, event.keycode)
    print(event)

root.bind("z", key_handler)
root.bind("Z", key_handler)

root.mainloop()