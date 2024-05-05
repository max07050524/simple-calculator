def calculate():
    if z == '+':
        print(x + y)
    elif z == '-':
        print(x - y)
    elif z == '*':
        print(x * y)
    elif z == '/':
        print(x / y)
    else:
        print('Error!')


x = int(input("What's the 1st number? "))
y = int(input("What's the 2nd number? "))
z = input("Which operator? ")

calculate()
