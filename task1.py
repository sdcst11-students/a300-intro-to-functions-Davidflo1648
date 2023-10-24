def A():
    print("You choose function A!")

def B():
    print("You choose function B!")

def C():
    print("You choose function C!")

userInput = input("Choose between A, B, and C: ")

if userInput == "A" or userInput == "a":
    A()
elif userInput == "B" or userInput == "b":
    B()
elif userInput == "C" or userInput == "c":
    C()