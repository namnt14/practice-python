import time
def years():
    name = input("Enter your name: ")
    age = int(input("Input your age: "))
    curYear = time.localtime(time.time())
    year = str(int(curYear[0]) + (100 - age))
    times = int(input ("How many times would you like the message to print out: "))
    message = name + " would turn into 100 years old in the year " + year + "\n"
    print(times * message)
