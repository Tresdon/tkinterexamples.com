import tkinter

root = tkinter.Tk()

tkinter.Label(root, text="Hello, World!").pack()

text_var = tkinter.StringVar()
text_var.set("Hello from a variable!")
tkinter.Label(root, textvariable=text_var).pack()

root.mainloop()
