def temperature_converter(number, unit_from, unit_to):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    if unit_from == 'c':
        c = number
    elif unit_from == 'f':
        c = (number - 32) * 5/9
    elif unit_from == 'k':
        c = number - 273.15
    elif unit_from == 'r':
        c = (number - 491.67) * 5/9
    elif unit_from == 're':
        c = number * 1.25
    elif unit_from == 'ro':
        c = (number - 7.5) * 40/21
    else:
        return None

    if unit_to == 'c':
        return c
    elif unit_to == 'f':
        return c * 9/5 + 32
    elif unit_to == 'k':
        return c + 273.15
    elif unit_to == 'r':
        return (c + 273.15) * 9/5
    elif unit_to == 're':
        return c * 0.8
    elif unit_to == 'ro':
        return c * 21/40 + 7.5

    return None


def length_converter(number, unit_from, unit_to):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    if unit_from == unit_to:
        return None

    if unit_from == 'cm':
        if unit_to == 'm': return number / 100
        if unit_to == 'dm': return number / 10
        if unit_to == 'mm': return number * 10
        if unit_to == 'km': return number / 100000
        if unit_to == 'in': return number / 2.54
        if unit_to == 'ft': return number / 30.48
        if unit_to == 'yd': return number / 91.44

    if unit_from == 'm':
        if unit_to == 'cm': return number * 100
        if unit_to == 'mm': return number * 1000
        if unit_to == 'km': return number / 1000
        if unit_to == 'in': return number * 39.3701
        if unit_to == 'ft': return number * 3.28084
        if unit_to == 'yd': return number * 1.09361

    if unit_from == 'mm':
        if unit_to == 'cm': return number / 10
        if unit_to == 'm': return number / 1000
        if unit_to == 'km': return number / 1000000
        if unit_to == 'in': return number / 25.4
        if unit_to == 'ft': return number / 304.8
        if unit_to == 'yd': return number / 914.4

    if unit_from == 'yd':
        if unit_to == 'cm': return number * 91.44
        if unit_to == 'm': return number * 0.9144
        if unit_to == 'mm': return number * 914.4
        if unit_to == 'km': return number * 0.0009144
        if unit_to == 'in': return number * 36
        if unit_to == 'ft': return number * 3

    if unit_from == 'in':
        if unit_to == 'cm': return number * 2.54
        if unit_to == 'm': return number * 0.0254
        if unit_to == 'mm': return number * 25.4
        if unit_to == 'km': return number * 0.0000254
        if unit_to == 'ft': return number / 12
        if unit_to == 'yd': return number / 36

    return None

while True:
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
                print(f"{number} {unit_from} = {result} {unit_to} rounded 4 digits")
                break
            else:
                print("Unsupported unit. Try again.")

    elif realm == '2':
        print("That's Temperature section:")

        while True:
            value = input("Input a temperature (e.g., 24 C or 42 F): ").strip().split()
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
            unit_to = input("Enter a target unit (C, F, K, R, Re, Ro): ").strip().lower()

            if unit_to == unit_from.lower():
                print("That's impossible. Try again.")
                continue

            result = temperature_converter(number, unit_from, unit_to)
            if result is not None:
                result = round(result, 4)
                print(f"{number} {unit_from.upper()} = {result} {unit_to.upper()} rounded 4 digits")
                break
            else:
                print("Unsupported unit. Try again.")
    loop = input("Would you like to go back and do some other conversation? (y/n): ").lower().strip()
    if loop == 'n':
        break
    elif loop == 'y':
        continue
