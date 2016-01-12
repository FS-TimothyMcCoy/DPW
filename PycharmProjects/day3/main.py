class Bird(object):
    def __init__(self):
        print "Bird created"
        self.wings = True
        self.name = ""
        self.food = "Worms"
    def fly(self):
        return "My name is " + self.name + ", Im Flapping my wings and flying!!"
    def eat(self):
        return "I am eating " + self.food

class Duck(Bird):
    def __init__(self):
        print "Duck created"
        super(Duck, self).__init__()
        self.bill = True
        self.webbed_feet = True
    def swim(self):
        return self.name + "is swimming with his webbed feet."

class Penguin(Bird):
        def __init__(self):
            print "Penguin created"
            super(Penguin, self).__init__()
            self.pole = "North Pole"
        def fish(self):
            return self.name + " is fishing in the " + self.pole
        def fly(self):
            return self.name + " I can't fly dumb dumb"

class SuperDodo(Bird):
    def __init__(self):
        print "SuperDodo created"
        super(SuperDodo, self).__init__()
    def fly(self):
        return super(SuperDodo, self).fly() + " and I'm shitting backwards!!!"



d = Duck()
p = Penguin()
p2 = Penguin()
sd = SuperDodo()
sd.name = "Scott"
d.name = "Daffy"
p.name = "Rico"
p2.name = "Kowalski"
print d.fly()
print d.eat()
print p.fish()
print p.fly()
print sd.fly()

