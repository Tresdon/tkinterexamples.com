# Empty Frame
import tkinter

root = tkinter.Tk()

tkinter.Frame(root).pack()

root.mainloop()


# Headless
import tkinter

root = tkinter.Tk()
root.withdraw()

root.mainloop()


# Frame with dimensions
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

tkinter.Frame(root, width=100, height=100).pack()

root.mainloop()



# With Items
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")


frame = tkinter.Frame(root)
frame.pack()

tkinter.Label(frame, text="INSIDE A FRAME :)").pack()

root.mainloop()
