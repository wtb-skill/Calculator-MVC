import tkinter as tk
from tkinter import ttk


class View(tk.Tk):

    PAD = 10

    def __init__(self, controller):
        super().__init__()
        self.controller = controller


        self.title('Calculator')


    def main(self):
        self.mainloop()



