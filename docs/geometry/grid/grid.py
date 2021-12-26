# Mistake
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

tkinter.Label(root, text="Label 1").grid(row=0, column=0)
tkinter.Label(root, text="Label 2").grid(row=0, column=0)

root.mainloop()




# Basic
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

for row in range(3):
    for col in range(3):
        tkinter.Label(root, text=f"{row},{col}", fg="navy").grid(row=row, column=col, padx=10)

root.mainloop()






# Rowspan
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

tkinter.Label(root, text="span2", bg="navy", fg="white").grid(row=0, column=1, rowspan=2)

# rowspan=1 is the default
tkinter.Label(root, text="span1", bg="darkred", fg="white").grid(row=0, column=0)
tkinter.Label(root, text="span1", bg="darkgreen", fg="white").grid(row=1, column=0)

root.mainloop()



# Column Span
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

tkinter.Label(root, text="span2", bg="navy", fg="white").grid(row=1, column=0, columnspan=2)

# columnspan=1 is the default
tkinter.Label(root, text="span1", bg="darkred", fg="white").grid(row=0, column=0)
tkinter.Label(root, text="span1", bg="darkgreen", fg="white").grid(row=0, column=1)

root.mainloop()





# Sticky
import tkinter

root = tkinter.Tk()
root.title("tkinterexamples.com")

# Padding
tkinter.Label(root, text="~~~~~~~~~~~", bg="navy", fg="white").grid(row=0, column=0)
tkinter.Label(root, text="~~~~~~~~~~~", bg="navy", fg="white").grid(row=0, column=1)

tkinter.Label(root, text="W", bg="navy", fg="white").grid(row=1, column=0, sticky=tkinter.W)
tkinter.Label(root, text="E", bg="navy", fg="white").grid(row=1, column=1, sticky=tkinter.E)

# Padding
tkinter.Label(root, text="~~~~~~~~~~~", bg="navy", fg="white").grid(row=2, column=0)
tkinter.Label(root, text="~~~~~~~~~~~", bg="navy", fg="white").grid(row=2, column=1)
tkinter.Label(root, text="CENTER", bg="navy", fg="white").grid(row=3, column=0, sticky="")
tkinter.Label(root, text="E + W", bg="navy", fg="white").grid(row=3, column=1, sticky=tkinter.NS)


root.mainloop()


