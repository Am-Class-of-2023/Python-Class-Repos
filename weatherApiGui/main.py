import tkinter as tk
from tkinter import *

root = tk.Tk()

def Window():
    window_width = "720"
    window_height = "480"
    canvas = Canvas(root, bg="White", width=window_width, height=window_height)
    root.title("Weather App")
    
    root.geometry(f"{window_width}x{window_height}")

Window()
root.mainloop()
