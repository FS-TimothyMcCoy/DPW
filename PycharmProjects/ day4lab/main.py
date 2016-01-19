class Controller(object):
    def __init__(self):
        print "Controller created"
        self.model = Model()
        self.view = View()
        d = self.model.get_messages()
        self.view.set_data(d)
        self.view.display_data()
        self.model.set_messages(0)
        print self.model.get_messages()

class Model(object):
    def __init__(self):
        print "Model created"
        self.pin = int(raw_input("What is your pin?"))
        self.__messages = 3
    def get_messages(self):
        if self.pin == 4201:
            return self.__messages
        else:
            return "Stop trying to read my messages bro"
    def set_messages(self, value):
        if self.pin == 4201 and value == 0:
            self.__messages = value
            print "Messages successfully deleted."
        else:
            print "You either did not have the correct credentials or did not set your messages to 0 to erase them."


class View(object):
    def __init__(self):
        print "View created"
        self.messages = 0
    def set_data(self, ms):
        self.messages = ms
    def display_data(self):
        print self.messages



c = Controller()
