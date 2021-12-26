# Absolute Position
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

tkinter.Label(root, text="x=50, y=50").place(x=50, y=50)
tkinter.Label(root, text="x=50, y=100").place(x=50, y=100)
tkinter.Label(root, text="x=150, y=75").place(x=150, y=75)

root.mainloop()




# Relative Position
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

# Add a frame
frame = tkinter.Frame(root, height=200, width=200, bg="navy")
frame.place(x=50, y=50)

tkinter.Label(frame, text="relx=0, rely=0").place(relx=0, rely=0)
tkinter.Label(frame, text="relx=0.4, rely=0.6").place(relx=0.4, rely=0.6)
tkinter.Label(frame, text="relx=1, rely=1").place(relx=1, rely=1)

root.mainloop()



# Centering
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

# Add a frame
frame = tkinter.Frame(root, height=200, width=200, bg="navy")
frame.place(x=50, y=50)

tkinter.Label(frame, text="I am centered.. Omm").place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()



# Absolute Size
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

# Add a frame
frame = tkinter.Frame(root, height=200, width=200, bg="navy")
frame.place(x=50, y=50)
label = tkinter.Label(frame, text="height=100\nwidth=100\n\nframe is\n200x200")
label.place(height=100, width=100, relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()




# Relative Size
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

# Add a frame
frame = tkinter.Frame(root, height=200, width=200, bg="navy")
frame.place(x=50, y=50)
label = tkinter.Label(frame, text="relheight=0.4\nrelwidth=0.7\n\nframe is\n200x200")
label.place(relheight=0.4, relwidth=0.7, relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()
