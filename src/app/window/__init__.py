import tkinter as tk
from tkinter import ttk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

root = tk.Tk()

window = App(root)

root.title('Task Controller')
root.minsize(height=720,width=1280)
root.maxsize(height=1080,width=1920)

window.mainloop()