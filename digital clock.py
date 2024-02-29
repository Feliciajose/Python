import tkinter as tk
import time

def clock():
    current=time.strftime("%H:%M:%S")
    label1["text"]=current
    root.after(1000,clock)
    
root=tk.Tk()
root.title("clock")
label1=tk.Label(root,font="article 80",bg="pink",fg="black")
label1.grid(row=0,column=0)
clock()
root.mainloop()