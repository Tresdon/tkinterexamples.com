import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

root.bind("<Button>", lambda event: print(event.num))

def enter_handler(event):
    event.widget.config(bg="navy", fg="white")
    print(event.x, event.y, event.x_root, event.y_root)

def leave_handler(event):
    event.widget.config(bg="white", fg="navy")
    print(event.x, event.y, event.x_root, event.y_root)



label = tkinter.Label(root, text="HELLO", bg="white", fg="navy")
label.bind("<Enter>", enter_handler)
label.bind("<Leave>", leave_handler)
label.pack()

root.mainloop()





# Protocol
import tkinter

root = tkinter.Tk()
root.protocol("WM_DELETE_WINDOW", root.destroy)

root.mainloop()