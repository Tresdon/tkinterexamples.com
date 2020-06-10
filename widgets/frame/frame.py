import tkinter

root = tkinter.Tk()

# Set up frames
left_frame = tkinter.Frame(root)
left_frame.pack(side=tkinter.LEFT)
right_frame = tkinter.Frame(root)
right_frame.pack(side=tkinter.RIGHT)

# Add labels
tkinter.Label(left_frame, text="LEFT").pack()
tkinter.Label(right_frame, text="RIGHT").pack()

root.mainloop()
