def string_both_ends(str):
    if len(str) < 2:
        return 'Your string is too short!'
    return str[0:2] + str[-2:]
    
string = input("Please enter a string: ")
stringToReturn = string_both_ends(string)
print(stringToReturn)