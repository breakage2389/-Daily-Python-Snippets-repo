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
print("Welcome to Calculator")
print('1 is add')
print('2 is sub')
print('3 is mul')
print('4 is div')
print('5 is pow')
try:
    choice = input("Enter your choice: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print(f'{num1} + {num2} = {add(num1, num2)}')
    elif choice == '2':
        if num1 > num2:
            print(f'{num1} - {num2} = {sub(num1, num2)}')
        elif num1 < num2:
            print(f'{num2} - {num1} = {mul(num2, num1)}')
        else:
            print(f'{num1} - {num2} = {div(num2, num1)}')
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

except ValueError:
    print("Please enter a number or your choice.")
    #continue
except ZeroDivisionError:
    print("Please enter a number or your choice.")
    #continue

