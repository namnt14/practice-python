def is_Palindrome(string):
    str1 = ""
    i = len(string) - 1
    while (i >= 0):
        str1 = str1 + string[i]
        i -= 1
    if (str1 == string):
        return True
    return False

def remove_special_characters(string):
    #remove white space
    while True:
        i = string.find(" ")
        if (i == -1):
            break
        string = string[0:i] + string[i+1:]
    #remove ','
    while True:
        i = string.find(",")
        if (i == -1):
            break
        string = string[0:i] + string[i+1:]
    #remove '''
    while True:
        i = string.find("'")
        if (i == -1):
            break
        string = string[0:i] + string[i+1:]
    #remove '?'
    while True:
        i = string.find("?")
        if (i == -1):
            break
        string = string[0:i] + string[i+1:]
    #remove '!'
    while True:
        i = string.find("!")
        if (i == -1):
            break
        string = string[0:i] + string[i+1:]
    #remove '.'
    while True:
        i = string.find(".")
        if (i == -1):
            break
        string = string[0:i] + string[i+1:]
    string = string.lower()
    return string     

def remove_special_characters1(string):
    #remove " ,'?!"
    while True:
        i1 = string.find(",")
        i2 = string.find("'")
        i3 = string.find(" ")
        i4 = string.find("?")
        i5 = string.find("!")
        i6 = string.find(".")
        if ((i1 == -1) and (i2 == -1) and (i3 == -1) and (i4 == -1) and (i5 == -1) and (i6 == -1)):
            break
        if (i1 != -1):
            string = string[0:i1] + string[i1+1:]
            continue
        if (i2 != -1):
            string = string[0:i2] + string[i2+1:]
            continue
        if (i3 != -1):
            string = string[0:i3] + string[i3+1:]
            continue
        if (i4 != -1):
            string = string[0:i4] + string[i4+1:]
            continue
        if (i5 != -1):
            string = string[0:i5] + string[i5+1:]
            continue
        if (i6 != -1):
            string = string[0:i6] + string[i6+1:]
            continue
    string = string.lower()
    return string     

def string_lists():
    string = str(input("Enter a string:"))
    string = remove_special_characters1(string)
    if is_Palindrome(string):
        print("Yes, this string is a palindrom")
    else:
        print("No, this string is NOT a palindrom") 
        
