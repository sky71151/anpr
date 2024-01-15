import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename='darkly')
b1 = ttk.Button(root, text='primary', bootstyle= SUCCESS)
b1.pack(side='left', padx=5, pady=10)

b2 = ttk.Button(root, text='secondary', bootstyle= (INFO, 'outline'))
b2.pack(side='left', padx=5, pady=10)
root.mainloop()
