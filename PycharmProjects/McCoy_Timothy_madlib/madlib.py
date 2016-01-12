def story(MyArr, MadlibDictionary):
        madlib = "There was a " + MyArr[2] + " foot long snake. "
        if int(MyArr[0]) >= 18 and MyArr[1] == "male":
            madlib += "He can open the door. So he did and when he opened it their " + MadlibDictionary["organ"] + " was lying on the ground. He felt their pulse and their heart beat "
            madlib += MadlibDictionary["pulseNumber"] + " times. Then he found " + MadlibDictionary["fingerNumber"] + " fingers on the ground next to the body. "
            madlib += "He then called " + MadlibDictionary["friendNumber"] + " friends. After alerting the police and finally took a " + MadlibDictionary["cleaning"] + " and went to bed."
        elif int(MyArr[0]) >= 18 and MyArr[1] == "female":
            madlib += "She can open the door. So she did and when she opened it their " + MadlibDictionary["organ"] + "was lying on the ground. She felt their pulse and their heart beat "
            madlib += MadlibDictionary["pulseNumber"] + " times. Then she found " + MadlibDictionary["fingerNumber"] + "fingers on the ground next to the body. "
            madlib += "She then called " + MadlibDictionary["friendNumber"] + " friends After alerting the police and finally took a " + MadlibDictionary["cleaning"] + " and went to bed."
        elif int(MyArr[0]) < 18 and MyArr[1] == "male":
            madlib += "He is not old enough to see what lies behind this door thus there is no story."
        elif int(MyArr[0]) < 18 and MyArr[1] == "female":
            madlib += "She is not old enough to see what lies behind this door thus there is no story."
        else:
            print "Double check your spelling and make sure there are no blanks."
        return madlib

numOfEncounters = raw_input("How many encounters were there?")

for i in range(0, int(numOfEncounters)):
    MyArr = []
    MyArr.append(raw_input("Please enter your age."))
    MyArr.append(raw_input("Please enter your gender (lower case)"))
    MyArr.append(raw_input("How long was the animal?"))
    MadlibDictionary = {"organ": raw_input("Please enter an organ from the human body."), "pulseNumber": raw_input("Please enter the number of times you felt the pulse."), "fingerNumber": raw_input("Please enter the number of fingers you saw near the body."), "friendNumber": raw_input("Enter the number of friends you called that night."), "cleaning": raw_input("Did you take a bath or a shower?")}
    print "/n"
    print story(MyArr, MadlibDictionary)