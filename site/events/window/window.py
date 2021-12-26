# Configure
import tkinter

root = tkinter.Tk()

def configure_handler(event):
    print(event)

root.bind("<Configure>", configure_handler)

root.mainloop()



# WM_DELETE_WINDOW
import tkinter
from tkinter import messagebox

root = tkinter.Tk()

def window_exit():
    close = messagebox.askyesno("", "Are you sure you want to exit?")
    if close:
        root.destroy()

root.protocol("WM_DELETE_WINDOW", window_exit)

root.mainloop()