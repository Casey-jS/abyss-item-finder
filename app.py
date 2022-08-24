import finder as f
import gui as g
import controller as c
import tkinter as tk

# Window class that we put the frame (gui) in
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Abyss Item Finder")
        self.geometry('600x200')
        self.config(bg="#565656")
        self.resizable(False, False)

        # create instances of model, view, controller
        model = f.Finder(self, "default")   
        view = g.GUI(self)
        view.grid_propagate(False)
        controller = c.Controller(model, view)
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()