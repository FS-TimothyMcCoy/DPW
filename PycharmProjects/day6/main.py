class Person(object):
    def __init__(self):
        print "Person Created"
        self.name = "TJ"
        self.age = 21
        self.__ssn = 2429843315

    def breathe(self):
        print "I'm Breathing"
    def sleep(self):
        return  "I'm snoring" + self.name

    def get_ssn(self):
        if self.age > 18:
            return self.__ssn
        else:
            return "Access Denied."

    def set_ssn(self):
        if self.age > 18:
            self.__ssn = int(raw_input("SSN: "))


class Student(Person):
    def __init__(self):
        super(Student, self).__init__()
        print "Student Created"
        self.grades = []
        self.id = 0
        self.degree = ""
        self.computer = Computer() # This is composition and aggregation instantiate a class inside of a class
    def study(self):
        pass
    def sleep(self):
        print super(Student, self).sleep()
        return "Sleep??? Nah"


class Computer(object):
    def __init__(self):
        print "Computer Created"







s = Student()
s.breathe()
print s.name
print s.get_ssn()
print s.set_ssn()
print s.sleep()











