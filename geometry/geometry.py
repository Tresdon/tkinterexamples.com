# Pack
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

tkinter.Label(root, text="Packed in here").pack()
tkinter.Button(root, text="Like").pack()
tkinter.Label(root, text="Sardines!!!").pack()

root.mainloop()


# Grid
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

tkinter.Label(root, text="Everything").grid(row=0, column=0)
tkinter.Label(root, text="In Its").grid(row=0, column=1)
tkinter.Button(root, text="Right").grid(row=1, column=0)
tkinter.Label(root, text="Place").grid(row=1, column=1)

root.mainloop()



# Place
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

tkinter.Label(root, text="Scattered").place(x=10, y=10)
tkinter.Button(root, text="all").place(x=50, y=30)
tkinter.Label(root, text="about").place(x=120, y=75)

root.mainloop()