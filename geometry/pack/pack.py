
# No arguments
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

tkinter.Label(root, text="Label").pack()
tkinter.Button(root, text="Button").pack()
tkinter.Entry(root, text="Entry").pack()

root.mainloop()


# Side=
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

tkinter.Label(root, text="RIGHT").pack(side=tkinter.RIGHT)
tkinter.Label(root, text="TOP").pack(side=tkinter.TOP)
tkinter.Label(root, text="LEFT").pack(side=tkinter.LEFT)
tkinter.Label(root, text="BOTTOM").pack(side=tkinter.BOTTOM)

root.mainloop()



# expand=
import tkinter

root = tkinter.Tk()
root.geometry("200x200")
root.title("tkinterexamples.com")

tkinter.Label(root, text="NATURAL", bg="navy", fg="white").pack()
tkinter.Label(root, text="EXPANDED", bg="navy", fg="white").pack(expand=True)

root.mainloop()



# fill=
import tkinter

root = tkinter.Tk()
root.geometry("300x300")
root.title("tkinterexamples.com")

tkinter.Label(root, text="Fill X", bg="darkred", fg="white").pack(fill=tkinter.X)
tkinter.Label(root, text="Fill Y", bg="navy", fg="white").pack(side=tkinter.LEFT, fill=tkinter.Y)
tkinter.Label(root, text="Fill BOTH", bg="darkgreen", fg="white").pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)
tkinter.Label(root, text="Fill None", bg="black", fg="white").pack(side=tkinter.BOTTOM, fill=tkinter.NONE)

root.mainloop()



# fill incorrect
import tkinter

root = tkinter.Tk()
root.geometry("300x300")
root.title("tkinterexamples.com")

tkinter.Label(root, text="Fill Y", bg="darkred", fg="white").pack(fill=tkinter.Y)
tkinter.Label(root, text="Fill X", bg="navy", fg="white").pack(side=tkinter.LEFT, fill=tkinter.X)
tkinter.Label(root, text="Fill BOTH", bg="darkgreen", fg="white").pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
tkinter.Label(root, text="Fill None", bg="black", fg="white").pack(side=tkinter.BOTTOM, fill=tkinter.NONE)

root.mainloop()