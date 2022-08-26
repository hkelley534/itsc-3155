def find_numbers(num1, num2):
    list = []

    for x in range(num1,num2):
        if(x%7==0 and not(x%5==0)):
            list.append(str(x))
    return list

num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

numbers = find_numbers(num1,num2)

print(','.join(numbers))

