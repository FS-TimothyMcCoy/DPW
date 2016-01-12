#function
def story(MadlibArr, MadlibDictionary): #This is a function in python def is the equivelant of function in js. It accepts 2 parameters which are used later.
    madlib = "There was a " + MadlibArr[0] + " year old, " + MadlibArr[1] + ". " #this declares a variable madlib and sets its initial value
    if int(MadlibArr[0]) >= 21 and MadlibArr[1] == "male": #conditional statement with a logical operator to test if the user inputted data matches those conditions
        madlib += "He can go to the bar! So he went. When he got there " + MadlibDictionary["movie"] + " was playing on the tv. He went to the counter and promptly ordered "
        madlib += MadlibDictionary["numOfBeer"] + " " + MadlibDictionary["beer"] + "(s). After drinking all of his " + MadlibDictionary["beer"] + "(s) he "
        madlib += "also ordered " + MadlibDictionary["numOfItem"] + " plates of " + MadlibDictionary["food"] + ". After finishing the movie he paid his tab and left." #This line and the two above concatenate more to the madlib variable.
    elif int(MadlibArr[0]) >= 21 and MadlibArr[1] == "female": #elif is the python equivelant of else if in js, testing to see if the MadlibArr with index of 1 is set to female
        madlib += "She can go to the bar! So she went. When she got there " + MadlibDictionary["movie"] + " was playing on the tv. She went to the counter and promptly ordered "
        madlib += MadlibDictionary["numOfBeer"] + " " + MadlibDictionary["beer"] + "(s). After drinking all of her " + MadlibDictionary["beer"] + "(s) she "
        madlib += "also ordered " + MadlibDictionary["numOfItem"] + " plates of " + MadlibDictionary["food"] + ". After finishing the movie she paid his tab and left."#This line and the two above concatenate more to the madlib variable.
    elif int(MadlibArr[0]) < 21 and MadlibArr[1] == "male": #again this compares the values of the user input data against defined data
        madlib += "He can not go to the bar and there is no story to be had here!" #concatenates more on to the madlib variable
    elif int(MadlibArr[0]) < 21 and MadlibArr[1] == "female": #comapres the values of the usier input data against defined data
        madlib += "She can not go to the bar and there is no story to be had here!" #concatenates more on to the madlib variable
    else: #catch all statement
        print "Please double check spelling and that you didn't input a blank." #prints the catch all statement
    return madlib #returns the madlib variable after the function is called and finishes





numOfStories = raw_input("How many stories would you like?") #sets a variable to user input



for i in range(0,int(numOfStories)): #for loop, declares i in scope, starting value is 0, end value is set to a casted variable. Uses default increment +1
    madlibArr = [] #delcares an array literal
    madlibArr.append(raw_input("Please enter an age.")) #appends a new item into the array that is user input
    madlibArr.append(raw_input("Please enter either male or female. (lower case)")) #appends a new item into the array that is user input
    madlibDictionary = {"movie": raw_input("Please enter a movie."), "numOfBeer": raw_input("Please enter a number."), "beer": raw_input("Please enter a type of beer."), "numOfItem": raw_input("Please enter a number."), "food": raw_input("Please enter a food.")}
    #the above line is like an array, but instead of a numerical index, there are key and values to the key. I have multiple keys each have 1 value that is user input
    print "\n" #prints a new line, \n is the escape character for new line
    print story(madlibArr, madlibDictionary) #captures the return value of the story function and prints it. This is also a function call that accepts two parameters.