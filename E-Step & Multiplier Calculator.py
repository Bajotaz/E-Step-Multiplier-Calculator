import tkinter as tk
from tkinter import *

def show_entry_fields():
    v1 = float(e1.get())
    v2 = float(e2.get())
    v3 = float(e3.get())
    c1 = v2/v3
    r1 = c1*v1
    v7 = round(r1,2)
    if v2 == v3:
        t2.delete(0, 'end')
        t2.insert(0, 'Use Current value')
    else:
        t2.delete(0, 'end')
        t2.insert(0, v7)

def show_entry_fields_3():
    v1 = float(e1.get())
    v2 = float(e2.get())
    v3 = float(e3.get())
    c1 = v3/v2
    r1 = c1*v1
    v7 = round(r1,6)
    if v2 == v3:
        t2.delete(0, 'end')
        t2.insert(0, 'Use Current value')
    else:
        t2.delete(0, 'end')
        t2.insert(0, v7)

def show_entry_fields_2():
    v4 = float(e4.get())
    v5 = float(e5.get())
    v6 = float(e6.get())
    c3 = v4*v5
    r2 = c3/v6
    v8 = round(r2,4)
    if v5 == v6:
        t1.delete(0, 'end')
        t1.insert(0, 'Use Current value')
    else:
        t1.delete(0, 'end')
        t1.insert(0, v8)

master = tk.Tk()
master.title("E-Step & Multiplier Calc")
master.geometry("310x330")
tk.Label(master, text="Extrusion E-Step calc :").grid(row=0)
tk.Label(master, text="Current E-Step value").grid(row=1)
tk.Label(master, text="Intended length").grid(row=2)
tk.Label(master, text="Measured length").grid(row=3)
tk.Label(master, text="New E-Step value").grid(row=4, column=0)
#tk.Label(master, text="").grid(row=5)
tk.Label(master, text="Extrusion multiplier calc :").grid(row=9)
tk.Label(master, text="Slicer multiplier value").grid(row=10)
tk.Label(master, text="Slicer wall thickness").grid(row=11)
tk.Label(master, text="Wall thickness").grid(row=12)
tk.Label(master, text="New multiplier value").grid(row=13)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
t1 = tk.Entry(master)
t2 = tk.Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=10, column=1)
e5.grid(row=11, column=1)
e6.grid(row=12, column=1)
t1.grid(row=13, column=1)
t2.grid(row=4, column=1)

tk.Label(master, text="").grid(row=15)
tk.Label(master, text="E-Step & Multiplier Calculator").grid(row=16)
tk.Label(master, text="Bajotaz 2021").grid(row=16, column=1)
tk.Button(master, text='Quit', command=master.quit).grid(row=14, column=0, sticky=tk.N, pady=4)
tk.Button(master, text='Marlin E-Step', command=show_entry_fields).grid(row=5, column=1, sticky=tk.N,pady=4)
tk.Button(master, text='Klipper E-Step', command=show_entry_fields_3).grid(row=5, column=0, sticky=tk.E,pady=4)
tk.Button(master, text='Calculate Multiplier', command=show_entry_fields_2).grid(row=14, column=1, sticky=tk.N,pady=4)

tk.mainloop()
