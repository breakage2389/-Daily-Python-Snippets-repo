#that's Budget_Analyzer

class Budget_Analyzer:
    def __init__(self,manufacturer , model , price , year):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price
        self.year = year

    def display_info(self):
        print("Manufacturer: " + self.manufacturer)
        print("Model: " + self.model)
        print("Price: " + self.price)
        print("Year: " + self.year)

def most_expensive(list_of_products):






#main
budget = int(input("Enter the budget: "))


products = int(input("Enter the number of products: "))
list_products = []

for i in range(products):
    while True:
        try:
            print()
            print(f'PRODUCT: {i + 1}')
            manufacturer = input("Enter the manufacturer: ")
            model = input("Enter the model: ")
            price = float(input("Enter the price of the product: "))
            year = int(input("Enter the year of the product: "))
            list_products.append(Budget_Analyzer(manufacturer, model, price, year))
            break
        except ValueError:
            print("Please enter the data correctly.")
        except ZeroDivisionError:
            print("Please enter a number or your choice.")
        except Exception as e:
            print(e)

list_money_for_products = [x.price for x in list_products]
print(list_money_for_products)
sum_price = sum(list_money_for_products)

if budget >= sum_price:
    print(f"You have enough money! And your remaining budget is {budget-sum_price}. ")
else:
    print(f"You don't have enough money!Your budget is {budget} and your whole price of the products is {sum_price}.")