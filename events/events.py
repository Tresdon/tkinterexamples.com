# Protocol
import tkinter

root = tkinter.Tk()
root.protocol("WM_DELETE_WINDOW", root.destroy)

root.mainloop()