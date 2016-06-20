def user_input_list():
    l =[]
    print("Enter a list of integers. Input 'Q' or 'q' to stop.")
    while True:
        user_input = input()
        if (user_input == 'Q' or user_input == 'q'):
            break;
        l.append(int(user_input))

    return l
    
def less_than_five():

    l = user_input_list()
    for element in l:
        if (element <= 5):
            print(element, end=" ", flush=True)
