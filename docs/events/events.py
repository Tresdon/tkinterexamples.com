# Implicit
import tkinter

root = tkinter.Tk()


tkinter.Checkbutton(root, command=lambda: print("x")).pack()
tkinter.Radiobutton(root, command=lambda: print("x")).pack()
tkinter.Scale(root, command=lambda x: print("x")).pack()
tkinter.Scrollbar(root, command=lambda x: print("x")).pack()
tkinter.Spinbox(root, command=lambda: print("x")).pack()

root.mainloop()


# Protocol
import tkinter

root = tkinter.Tk()
root.protocol("WM_DELETE_WINDOW", root.destroy)

root.mainloop()