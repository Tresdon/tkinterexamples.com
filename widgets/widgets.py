# Label
from PIL import Image, ImageTk
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

# change label colors
tkinter.Label(root, fg="navy", text="blue text!").pack()
tkinter.Label(root, bg="navy", fg="white", text="blue background :)").pack()

# Add padding to a label to help it breathe
tkinter.Label(root, text="text with padding", pady=10).pack()

# Change the font of a label
tkinter.Label(root, text="helvetica 20", font=("Helvetica", 20)).pack()

# Image and text combined
image = ImageTk.PhotoImage(Image.open("/Users/tresdon/Downloads/wave.png").resize((200,200)))
tkinter.Label(root, text="the great wave", image=image, compound=tkinter.LEFT).pack()

root.mainloop()





# Frame
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

# Set up our frames
left_frame = tkinter.Frame(root, borderwidth=5, relief=tkinter.RIDGE)
left_frame.pack(side=tkinter.LEFT)
right_frame = tkinter.Frame(root, background="navy", padx=20, pady=20)
right_frame.pack(side=tkinter.RIGHT)

# Add items to the left frame
tkinter.Label(left_frame, text="I'm a label in the left frame").pack()
tkinter.Button(left_frame, text="Left frame rules!").pack()

# Add items to the right frame
tkinter.Label(right_frame, text="and I'm in the right frame").pack()
tkinter.Button(right_frame, text="right frame best frame!").pack()
 
root.mainloop()





# Button
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

tkinter.Button(root, text="Plain Button", command=lambda: print("hello!")).pack()
tkinter.Button(root, text="Button with some style", \
font=("Times", 20), fg="navy", activeforeground="navy").pack()
tkinter.Button(root, text="tall button", height=10).pack()
tkinter.Button(root, text="wide button", width=20).pack()
 
root.mainloop()