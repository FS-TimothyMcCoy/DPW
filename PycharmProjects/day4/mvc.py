# ----------- Controller Class
class Controller(object):
    def __init__(self):
        print "Controller created"
        self.model = Model() #connection between cont. and model
        self.view = View()  #connection between cont. and view
        d = self.model.get_data()  # d catches the returned data
        self.view.set_data(d)
        self.view.display_data()


# ----------- Model Class
class Model(object):
    def __init__(self):
        print "Model Created"
        # data held within a dictionary
        self.data = {"make": "Toyota", "model": "Camry", "price": 22000}
    def get_data(self):
        return self.data  # return data to the controller


# ------------ View Class
class View(object):
    def __init__(self):
        print "View Created"
        self.data = 0
    def set_data(self, dt):
        self.data = dt # sets data in view equal to dt
    def display_data(self):
        print self.data



c = Controller()
