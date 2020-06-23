import time
import threading

import tkinter

root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()

def fade():
    global frame
    # Walk backwards through opacities (255 is opaque, 0 is transparent)
    i = 1.0
    while i >= 0:
        frame.parent.attributes("-alpha", i)
        i -= 0.1
        # Sleep some time to make the transition not immediate
        time.sleep(0.05)
    
# Put image fading in a thread so it doesn't block our GUI
fade_thread = threading.Thread(target=fade)
tkinter.Button(frame, text="Fade out", command=fade_thread.start).pack()

root.mainloop()