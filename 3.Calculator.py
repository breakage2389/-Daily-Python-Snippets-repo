def add(a,b):

    return a+b

def sub(a,b):

    return a-b

def mul(a,b):

    return a*b

def div(a,b):

    return a/b

def pow(a,b):

    return a**b
##MAIN

while True:
    try:
        print('1 is add')
        print('2 is sub')
        print('3 is mul')
        print('4 is div')
        print('5 is pow')
        choice = input("Enter your choice: ")
        x = choice.isnumeric()
        if not x == True:
            print("Invalid input.")
            raise ValueError

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f'{num1} + {num2} = {add(num1, num2)}')
        elif choice == '2':
            print(f'{num1} - {num2} = {sub(num1, num2)}')
        elif choice == '3':
            print(f'{num1} * {num2} = {pow(num1, num2)}')
        elif choice == '4':
            if num2 ==0:
                raise ZeroDivisionError
            else:
                print(f'{num1} / {num2} = {pow(num1, num2)}')
        elif choice == '5':
            print(f'{num1} ** {num2} = {pow(num1, num2)}')
        else:
            print("Unsupported unit.")

        choice1= input('Do you want to exit? (y/n)')
        if choice1 == 'y':
            print('Have a lovely day!')
            break
        elif choice1 == 'n':
            continue

    except ValueError:
        print("Please enter a number or your choice.")

    except ZeroDivisionError:
        print("Please enter a number or your choice.")


