# Clicking
import tkinter

root = tkinter.Tk()

def click_handler(event):
    # event also has x & y attributes
    if event.num == 2:
        print("RIGHT CLICK")

root.bind("<Button>", click_handler)
root.bind("<Button-1>", lambda x: print("LEFT CLICK"))

root.mainloop()




# Dragging
import tkinter

root = tkinter.Tk()
label = tkinter.Label(root, text="HEY")
label.pack()

def drag_handler(event):
    print(event.x, event.y)

label.bind("<B1-Motion>", drag_handler)

root.mainloop()



# Hovering
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

label = tkinter.Label(root, text="HELLO", bg="white", fg="navy")
label.bind("<Enter>", lambda event: event.widget.config(bg="navy", fg="white"))
label.bind("<Leave>", lambda event: event.widget.config(bg="white", fg="navy"))
label.pack()

root.mainloop()