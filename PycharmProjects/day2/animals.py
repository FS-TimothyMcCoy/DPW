class Dog():
    def __init__(self, n, a):
        print "Dog created"
        self.name = n
        self.breed = "Beagle"
        self.age = a
    def bark(self):
        return "Woof Woof " + self.name
    def run(self):
        return "I am " + str(self.age) + " years old, and I am frolicking!"

d1 = Dog("Fido", 7)
print d1.run()

print "-------"

d2 = Dog("Rex", 12)
print d2.run()
