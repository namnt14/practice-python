def odd_even():
    num = int(input("Enter a number to check: "))
    check = int(input("Enter another number to divide by: "))
    if (num % 2 == 0):
        print("%d is even." %(num))
    else:
        print("%d is odd." %(num))
    if (num % 4 == 0):
        print("%d is also a multiple of 4." %(num))
    if (num % check == 0):
        print("%d is divided evenly by %d." %(num,check))
    else:
        print("%d is not able to be divided evenly by %d." %(num,check))
