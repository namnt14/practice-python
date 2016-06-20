def find_divisors():
    num = int(input("Enter a number to find its divisors:"))
    l1 = range(1, num + 1)
    l2 = []
    for i in l1:
        if (num % i == 0):
            l2.append(i)
    print(l2)

        
