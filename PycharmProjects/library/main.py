from lib import Library, Printer


class Main_Handler():
    def __init__(self):
        l = Library()
        p = Printer()
        name = raw_input("What is your name?")
        fav_color = raw_input("What is your favorite color?")
        hair_color = raw_input("What is your hair color?")
        birth_year = int(raw_input("What year were you born?(4 digits)"))
        current_year = int(raw_input("What is the current year?(4 digits)"))
        age = l.get_age(current_year, birth_year)
        p.print_out(age)
        color = l.get_color(fav_color)
        p.print_color(color)
        haircolor = l.get_haircolor(hair_color)
        p.print_haircolor(haircolor)



main = Main_Handler()