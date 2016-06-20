def user_input_list():
    l =[]
    print("Enter a list of integers. Input 'Q' or 'q' to stop.")
    while True:
        user_input = input()
        if (user_input == 'Q' or user_input == 'q'):
            break;
        l.append(int(user_input))

    return l
    
def less_than():

    l = user_input_list()
    num = int(input("Choose a number to compare:"))
    for element in l:
        if (element <= num):
            print(element, end=" ", flush=True)
