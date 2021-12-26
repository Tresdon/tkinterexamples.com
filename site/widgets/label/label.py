# Static Text Label
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

tkinter.Label(root, text="Hello, world!").pack()

root.mainloop()


# Dynamic Text Label
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

text_var = tkinter.StringVar()
text_var.set("Hello from a variable!")
tkinter.Label(root, textvariable=text_var).pack()

root.mainloop()


# Image Label
import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title("tkinterexamples.com")

pil_image = Image.open("/Users/tresdon/images_synced/photographs/pentax/california/split_tree.jpg")
pil_image_resized = pil_image.resize((300, 200))
tkinter_image = ImageTk.PhotoImage(pil_image_resized)

tkinter.Label(root, image=tkinter_image).pack()

root.mainloop()