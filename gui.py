from tkinter import *
from tkinter import ttk
import tkinter as tk

# View (Frame to put on App window)
class GUI(ttk.Frame):

    # parent -> App window
    def __init__(self, parent):
        super().__init__(parent)

        # defaults
        self.default_colors = {"fg" : "#FF00FF", "bg" : "#565656"}
        self.middle_x = {"relx" : ".5", "anchor" : "center"}


        self.input = tk.StringVar()

        # Label to prompt for input
        self.prompt = Label(parent, self.default_colors, text = "Enter Item", font=("Arial Bold", 20))
        self.prompt.place(self.middle_x, rely = .05)

        # Search box
        self.name_entry = Entry(parent, self.default_colors, textvariable = self.input, font=("Arial Bold", 15), width = 16)
        self.name_entry.place(self.middle_x, rely = .2)

        self.description = Text(parent, self.default_colors, width = 40,  height = 4, wrap=WORD, font=("Arial Bold", 15))
        self.description.place(self.middle_x, rely = .7)
     
        self.submit_button = Button(parent, 
                        text="Submit", 
                        fg = "#FF00FF", 
                        highlightbackground="#565656", 
                        bg = "#565656", 
                        height = 1, 
                        width = 8, 
                        borderwidth = 2, 
                        relief="solid",
                        command = self.submit_clicked)

        self.submit_button.place(relx = .5, rely = .35, anchor = 'center')
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def submit_clicked(self):
        if self.controller:
            self.controller.find(self.input.get())
    
    # modify description box to only show most recent search result
    def show_desc(self, desc):
        self.description.delete('1.0', 'end')
        self.description.insert('1.0', desc)


