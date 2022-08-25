str = input("Please enter a string: ")

if len(str) < 2:
    print("String is too short!")
else:
    print(str[0:2]+str[-2:])

input()