class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def find(self, input):
        desc = self.model.find(input)
        self.view.show_desc(desc)