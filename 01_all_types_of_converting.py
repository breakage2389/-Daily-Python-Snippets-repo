def length_converter(number, unit_from, unit_to):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    if unit_from == unit_to:
        return None

    if unit_from == 'cm':
        if unit_to == 'm':
            return number / 100
        elif unit_to == 'dm':
            return number / 10
        elif unit_to == 'mm':
            return number * 10
        elif unit_to == 'km':
            return number / 100000
        elif unit_to == 'in':
            return number / 2.54
        elif unit_to == 'ft':
            return number / 30.48
        elif unit_to == 'yd':
            return number / 91.44

    if unit_from == 'm':
        if unit_to == 'cm':
            return number * 100
        elif unit_to == 'mm':
            return number * 1000
        elif unit_to == 'km':
            return number / 1000
        elif unit_to == 'in':
            return number * 39.3701
        elif unit_to == 'ft':
            return number * 3.28084
        elif unit_to == 'yd':
            return number * 1.09361

    if unit_from == 'mm':
        if unit_to == 'cm':
            return number / 10
        elif unit_to == 'm':
            return number / 1000
        elif unit_to == 'km':
            return number / 1000000
        elif unit_to == 'in':
            return number / 25.4
        elif unit_to == 'ft':
            return number / 304.8
        elif unit_to == 'yd':
            return number / 914.4

    if unit_from == 'yd':
        if unit_to == 'cm':
            return number * 91.44
        elif unit_to == 'm':
            return number * 0.9144
        elif unit_to == 'mm':
            return number * 914.4
        elif unit_to == 'km':
            return number * 0.0009144
        elif unit_to == 'in':
            return number * 36
        elif unit_to == 'ft':
            return number * 3


    return None

print('Type of realms: ',
      '\n1 -> Length / Distance', '2 -> Temperature', '3 -> Mass / Weight', '4 -> Volume / Capacity',
      '\n5 -> Area', '6 -> Speed / Velocity', '7 -> Time', '8 -> Energy',
      '\n9 -> Pressure', '10 -> Power', '11 -> Digital Storage / Data', '12 -> Angle')

realm = input("\nWhat type of converting do you want? (Number please): ")
while not realm.isdigit():
    realm = input("Enter a number please: ")

if realm == '1':
    print("That's Length/Distance section:")

    while True:
        value = input("Input a measurement (number + unit, e.g., 24 cm): ").strip().split()
        if len(value) != 2:
            print("Invalid format. Try again.")
            continue

        number_str, unit_from = value
        try:
            number = float(number_str)
        except ValueError:
            print("Invalid number. Try again.")
            continue

        break

    while True:
        unit_to = input("Enter a target unit (e.g., m, ft, in): ").strip().lower()
        if unit_to == unit_from.lower():
            print("That's impossible. Try again.")
            continue

        result = length_converter(number, unit_from, unit_to)
        if result is not None:
            result = round(result, 4)
            print(f"{number} {unit_from} = {result} {unit_to} rounded 4 digits after the comma")
            break
        else:
            print("Unsupported unit. Try again.")
