print('THE CURRENCY IS IN EURO / €')
class Product:
    def __init__(self, manufacturer, model, price, year):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price
        self.year = year

    def __str__(self):
        return f"{self.year} {self.manufacturer} {self.model} (€{self.price:,.2f})"

def most_expensive_product(inventory):
    inventory.sort(key=lambda x:x.price ,reverse=True)
    return inventory[0]


budget = float(input("Enter your total budget: "))
count = int(input("How many products are you adding? "))
inventory = []

for i in range(count):
    while True:
        try:
            print(f"\n--- Item {i + 1} ---")
            mfr = input("Manufacturer: ")
            mdl = input("Model: ")
            prc = float(input("Price: "))
            yr = int(input("Year: "))

            inventory.append(Product(mfr, mdl, prc, yr))
            break
        except ValueError:
            print("Invalid input. Please use numbers for price and year.")

total_cost = sum(item.price for item in inventory)

print("\n" + "=" * 20)
if budget >= total_cost:
    print(f"SUCCESS: Within budget!")
    print(f"Remaining: €{budget - total_cost:,.2f}")
else:
    print(f"OVER BUDGET: You are short by €{total_cost - budget:,.2f}")

print(f"Total Cost: €{total_cost:,.2f}")

print('the most expensive product-> ',most_expensive_product(inventory))
