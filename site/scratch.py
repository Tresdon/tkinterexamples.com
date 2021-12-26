import tkinter as tk
from PIL import ImageTk, Image

class Main(tk.Tk):
    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self,*args, *kwargs)
        self.config(bg='gray')
        self.title('Functionality')
        self.geometry('560x400')
        test_img = ImageTk.PhotoImage(Image.open('favicon.ico'))
        self.label2 = tk.Label(image=test_img)
        self.label2.photo = test_img
        self.label2.grid(column=1, row=0)
        self.label = tk.Label(self, text='Please Select a Choice Below', font=('Arial Bold', 30), bg='gray')
        self.label.grid(column=1, row=1)
        self.button_retorque = tk.Button(self, text='Re-torque', command=lambda: reTorque())
        self.button_retorque.grid(column=1, row=3, pady=10)
        self.quit = tk.Button(self, text='Close Application', command=self.destroy)
        self.quit.grid(column=1, row=5, pady=10)

class reTorque(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, *kwargs)
        self.config(bg='gray')
        self.geometry('750x400')
        self.label = tk.Label(self, text='This is for a Re-torque', font=('Arial Bold', 30), bg='gray')
        self.label.grid(column=0, row=0)
        self.button3 = tk.Button(self, text = 'Set Board Type Odd', command=boardOdd)
        self.button3.grid(column=0, row=1, pady=10)
        self.button = tk.Button(self,text='Close', command=self.destroy)
        self.button.grid(column=0, row=5)
        self.grab_set()

class boardOdd(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.config(bg='gray')
        self.geometry('500x400')
        self.label = tk.Label(self, text='Select Number of Odd Boards', font=('Arial Bold', 12), bg='gray')
        self.label.grid(column=0, row=0)
        odd_img = ImageTk.PhotoImage(Image.open('C:\\Users\\myuser\\Desktop\\Python Tests\\pics\\odd.jpg'))
        self.label2 = tk.Label(image=odd_img)
        self.label2.photo = odd_img
        self.label2.grid(column=2, row=0)
        self.button1 = tk.Button(self, text='1')
        self.button1.grid(column=0, row=1, pady=10)
        self.button2 = tk.Button(self, text='2')
        self.grab_set()

if __name__ == '__main__':
    app = Main()
    app.mainloop()