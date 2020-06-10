import tkinter

root = tkinter.Tk()

tkinter.Button(root, text="Click Me", command=lambda: print("HELLO")).pack()

root.mainloop()
