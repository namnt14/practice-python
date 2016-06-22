from random import randint
def create_list(length):
    l = []
    for i in range(0,length):
        i = randint(0,100)
        l.append(i)
    print(l)
    return set(l)

def list_overlap():
    length = int(input("Enter the length of the first list:"))
    l1 = create_list(length)
    length = int(input("Enter the length of the second list:"))
    l2 = create_list(length)
    match = []
    for i in l1:
        if (i in l2):
            match.append(i)
    print("The matching list should be:")
    print(match)
