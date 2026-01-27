def Energy(number, unit_from, unit_to):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    to_joules = {
        'j': 1,
        'kj': 1000,
        'cal': 4.184,
        'kcal': 4184,
        'wh': 3600,
        'kwh': 3600000
    }

    if unit_from not in to_joules or unit_to not in to_joules:
        return None

    joules = number * to_joules[unit_from]
    return joules / to_joules[unit_to]


def Pressure(number, unit_from, unit_to):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    to_pascal = {
        'pa': 1,
        'hpa': 100,
        'kpa': 1000,
        'bar': 100000,
        'psi': 6894.76,
        'atm': 101325
    }

    if unit_from not in to_pascal or unit_to not in to_pascal:
        return None

    pascal = number * to_pascal[unit_from]
    return pascal / to_pascal[unit_to]


def Power(number, unit_from, unit_to):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    to_watt = {
        'w': 1,
        'kw': 1000,
        'mw': 1000000,
        'hp': 745.7
    }

    if unit_from not in to_watt or unit_to not in to_watt:
        return None

    watt = number * to_watt[unit_from]
    return watt / to_watt[unit_to]


def Digital_storage(number, unit_from, unit_to):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    to_bytes = {
        'b': 1,
        'kb': 1024,
        'mb': 1024 ** 2,
        'gb': 1024 ** 3,
        'tb': 1024 ** 4
    }

    if unit_from not in to_bytes or unit_to not in to_bytes:
        return None

    bytes_val = number * to_bytes[unit_from]
    return bytes_val / to_bytes[unit_to]


def Angle(number, unit_from, unit_to):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()
    import math

    to_degrees = {
        'deg': 1,
        'rad': 180 / math.pi,
        'grad': 0.9
    }

    if unit_from not in to_degrees or unit_to not in to_degrees:
        return None

    degrees = number * to_degrees[unit_from]
    return degrees / to_degrees[unit_to]


def Time(number, unit_from, unit_to):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    if unit_from == unit_to:
        return number

    if unit_from == 'hour':
        if unit_to == 'minutes':
            return number * 60
        elif unit_to == 'seconds':
            return number * 3600
        elif unit_to == 'milliseconds':
            return number * 3600000

    elif unit_from == 'minutes':
        if unit_to == 'hour':
            return number / 60
        elif unit_to == 'seconds':
            return number * 60
        elif unit_to == 'milliseconds':
            return number * 60000

    elif unit_from == 'seconds':
        if unit_to == 'hour':
            return number / 3600
        elif unit_to == 'minutes':
            return number / 60
        elif unit_to == 'milliseconds':
            return number * 1000

    elif unit_from == 'milliseconds':
        if unit_to == 'hour':
            return number / 3600000
        elif unit_to == 'minutes':
            return number / 60000
        elif unit_to == 'seconds':
            return number / 1000

    return None


def Speed_converter(number, unit_from, unit_to):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    if unit_from == "km/h":
        if unit_to == "m/s":
            return number / 3.6
        if unit_to == "mph":
            return number / 1.609
    if unit_from == "m/s":
        if unit_to == "km/h":
            return number * 3.6
        if unit_to == "mph":
            return number * 2.237
    if unit_from == "mph":
        if unit_to == "km/h": return number * 1.609
        if unit_to == "m/s": return (number * 1.609) / 3.6

    return None


def volume_converter(number, unit_from, unit_to):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    to_liters = {
        'ml': number / 1000,
        'l': number,
        'm3': number * 1000,
        'cm3': number / 1000,
        'ft3': number * 28.3168,
        'in3': number * 0.0163871,
        'gal': number * 3.78541
    }

    if unit_from not in to_liters:
        return None

    liters = to_liters[unit_from]

    from_liters = {
        'ml': liters * 1000,
        'l': liters,
        'm3': liters / 1000,
        'cm3': liters * 1000,
        'ft3': liters / 28.3168,
        'in3': liters / 0.0163871,
        'gal': liters / 3.78541
    }

    return from_liters.get(unit_to)


def weight_mass_converter(number, unit_from, unit_to):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    if unit_from == unit_to:
        return None

    if unit_from == 'kg':
        if unit_to == 'g': return number * 1000
        if unit_to == 'mg': return number * 1_000_000
        if unit_to == 'lbs': return number * 2.20462
        if unit_to == 'ounces': return number * 35.274
        if unit_to == 'metric_ton': return number / 1000
        if unit_to == 'stone': return number / 6.35

    if unit_from == 'g':
        if unit_to == 'kg': return number / 1000
        if unit_to == 'mg': return number * 1000
        if unit_to == 'lbs': return number * 0.00220462
        if unit_to == 'ounces': return number * 0.035274
        if unit_to == 'metric_ton': return number / 1_000_000
        if unit_to == 'stone': return number / 6350

    if unit_from == 'mg':
        if unit_to == 'kg': return number / 1_000_000
        if unit_to == 'g': return number / 1000
        if unit_to == 'lbs': return number * 2.20462e-6
        if unit_to == 'ounces': return number * 3.5274e-5
        if unit_to == 'metric_ton': return number / 1_000_000_000
        if unit_to == 'stone': return number / 6_350_000

    if unit_from == 'lbs':
        if unit_to == 'kg': return number / 2.20462
        if unit_to == 'g': return number * 453.592
        if unit_to == 'mg': return number * 453_592
        if unit_to == 'ounces': return number * 16
        if unit_to == 'metric_ton': return number / 2204.62
        if unit_to == 'stone': return number / 14

    if unit_from == 'ounces':
        if unit_to == 'kg': return number / 35.274
        if unit_to == 'g': return number * 28.3495
        if unit_to == 'mg': return number * 28_349.5
        if unit_to == 'lbs': return number / 16
        if unit_to == 'metric_ton': return number / 35_274
        if unit_to == 'stone': return number / 224

    if unit_from == 'metric_ton':
        if unit_to == 'kg': return number * 1000
        if unit_to == 'g': return number * 1_000_000
        if unit_to == 'mg': return number * 1_000_000_000
        if unit_to == 'lbs': return number * 2204.62
        if unit_to == 'ounces': return number * 35274
        if unit_to == 'stone': return number * 157.473

    if unit_from == 'stone':
        if unit_to == 'kg': return number * 6.35
        if unit_to == 'g': return number * 6350
        if unit_to == 'mg': return number * 6_350_000
        if unit_to == 'lbs': return number * 14
        if unit_to == 'ounces': return number * 224
        if unit_to == 'metric_ton': return number * 0.00635

    return None


def temperature_converter(number, unit_from, unit_to):
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    if unit_from == 'c':
        c = number
    elif unit_from == 'f':
        c = (number - 32) * 5 / 9
    elif unit_from == 'k':
        c = number - 273.15
    elif unit_from == 'r':
        c = (number - 491.67) * 5 / 9
    elif unit_from == 're':
        c = number * 1.25
    elif unit_from == 'ro':
        c = (number - 7.5) * 40 / 21
    else:
        return None

    if unit_to == 'c':
        return c
    elif unit_to == 'f':
        return c * 9 / 5 + 32
    elif unit_to == 'k':
        return c + 273.15
    elif unit_to == 'r':
        return (c + 273.15) * 9 / 5
    elif unit_to == 're':
        return c * 0.8
    elif unit_to == 'ro':
        return c * 21 / 40 + 7.5

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


def area_converter(number, unit_from):
    unit_from = unit_from.lower()
    valid_units = {"mm", "cm", "m", "km", "yd", "in", "ft"}

    if unit_from not in valid_units:
        return None

    area = number * number
    return area


print('Type of realms: ',
      '\n1 -> Length / Distance', '2 -> Temperature', '3 -> Mass / Weight', '4 -> Volume / Capacity',
      '\n5 -> x -> x\u00b2', '6 -> Speed / Velocity', '7 -> Time', '8 -> Energy',
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
            break
        except ValueError:
            print("Invalid number. Try again.")
            continue
    while True:
        unit_to = input("Enter a target unit (e.g., m, ft, in): ").strip().lower()
        result = length_converter(number, unit_from, unit_to)
        if result is not None:
            print(f"{number} {unit_from} = {round(result, 4)} {unit_to} rounded 4 digits")
            break
        else:
            print("Unsupported unit. Try again.")

elif realm == '2':
    print("That's Temperature section:")
    while True:
        value = input("Input a temperature (e.g., 24 C): ").strip().split()
        if len(value) != 2:
            print("Invalid format. Try again.")
            continue
        number_str, unit_from = value
        try:
            number = float(number_str)
            break
        except ValueError:
            print("Invalid number. Try again.")
    while True:
        unit_to = input("Enter a target unit (C, F, K, R, Re, Ro): ").strip().lower()
        result = temperature_converter(number, unit_from, unit_to)
        if result is not None:
            print(f"{number} {unit_from.upper()} = {round(result, 4)} {unit_to.upper()} rounded 4 digits")
            break
        else:
            print("Unsupported unit. Try again.")

elif realm == '3':
    print("That's Mass / Weight:")
    while True:
        value = input("Input a mass / weight (e.g., 1 kg): ").strip().split()
        if len(value) != 2:
            print("Invalid format. Try again.")
            continue
        number_str, unit_from = value
        try:
            number = float(number_str)
            break
        except ValueError:
            print("Invalid number. Try again.")
    while True:
        unit_to = input("Enter a target unit (g, mg, kg, lbs, ounces, metric_ton, stone): ").strip().lower()
        result = weight_mass_converter(number, unit_from, unit_to)
        if result is not None:
            print(f'{number} {unit_from.upper()} = {round(result, 4)} {unit_to} rounded 4 digits')
            break
        else:
            print("Unsupported unit. Try again.")

elif realm == '4':
    print("That's Volume / Capacity:")
    while True:
        value = input("Input a volume (e.g., 2 l): ").strip().split()
        if len(value) != 2:
            print("Invalid format. Try again.")
            continue
        number_str, unit_from = value
        try:
            number = float(number_str)
            break
        except ValueError:
            print("Invalid number. Try again.")
    while True:
        unit_to = input("Enter a target unit (ml, l, m3, cm3, ft3, in3, gal): ").strip().lower()
        result = volume_converter(number, unit_from, unit_to)
        if result is not None:
            print(f"{number} {unit_from} = {round(result, 4)} {unit_to} rounded 4 digits")
            break
        else:
            print("Unsupported unit. Try again.")

elif realm == '5':
    print("x -> x\u00b2:")
    while True:
        value = input("Input a length (e.g., 150 cm): ").strip().split()
        if len(value) != 2:
            print("Invalid format. Try again.")
            continue
        number_str, unit_from = value
        try:
            number = float(number_str)
            break
        except ValueError:
            print("Invalid number. Try again.")
    result = area_converter(number, unit_from)
    if result is not None:
        print(f"{number} {unit_from} = {round(result, 4)} {unit_from}\u00b2 (rounded 4 digits)")
    else:
        print("Unsupported unit.")

elif realm == '6':
    print('That\'s Speed / Velocity section:')
    while True:
        value = input("Input a speed (e.g., 1 km/h): ").strip().split()
        if len(value) != 2:
            print("Invalid format. Try again.")
            continue
        number_str, unit_from = value
        try:
            number = float(number_str)
            break
        except ValueError:
            print("Invalid number. Try again.")
    while True:
        unit_to = input("Enter a target unit (km/h, m/s, mph): ").strip().lower()
        result = Speed_converter(number, unit_from, unit_to)
        if result is not None:
            print(f"{number} {unit_from} = {round(result, 4)} {unit_to} rounded 4 digits")
            break
        else:
            print("Unsupported unit. Try again.")

elif realm == '7':
    print('That\'s Time section:')
    while True:
        value = input('Input a time (e.g., 1 hour): ').strip().split()
        if len(value) != 2:
            print('Please enter valid time')
            continue
        number_str, unit_from = value
        try:
            number = float(number_str)
            break
        except ValueError:
            print("Invalid number. Try again.")
    while True:
        unit_to = input("Enter a target unit (hour, minutes, seconds, milliseconds): ").strip().lower()
        result = Time(number, unit_from, unit_to)
        if result is not None:
            print(f"{number} {unit_from} = {round(result, 4)} {unit_to} rounded 4 digits")
            break
        else:
            print("Unsupported unit. Try again.")

elif realm == '8':
    print('That\'s Energy section:')
    while True:
        value = input('Input energy (e.g., 100 j): ').strip().split()
        if len(value) != 2:
            print('Please enter valid format')
            continue
        number_str, unit_from = value
        try:
            number = float(number_str)
            break
        except ValueError:
            print("Invalid number. Try again.")
    while True:
        unit_to = input("Enter target unit (j, kj, cal, kcal, wh, kwh): ").strip().lower()
        result = Energy(number, unit_from, unit_to)
        if result is not None:
            print(f"{number} {unit_from} = {round(result, 4)} {unit_to} rounded 4 digits")
            break
        else:
            print("Unsupported unit. Try again.")

elif realm == '9':
    print('That\'s Pressure section:')
    while True:
        value = input('Input pressure (e.g., 1 bar): ').strip().split()
        if len(value) != 2:
            print('Please enter valid format')
            continue
        number_str, unit_from = value
        try:
            number = float(number_str)
            break
        except ValueError:
            print("Invalid number.")
    while True:
        unit_to = input("Enter target unit (pa, hpa, kpa, bar, psi, atm): ").strip().lower()
        result = Pressure(number, unit_from, unit_to)
        if result is not None:
            print(f"{number} {unit_from} = {round(result, 4)} {unit_to} rounded 4 digits")
            break
        else:
            print("Unsupported unit.")

elif realm == '10':
    print('That\'s Power section:')
    while True:
        value = input('Input power (e.g., 10 kw): ').strip().split()
        if len(value) != 2:
            continue
        number_str, unit_from = value
        try:
            number = float(number_str)
            break
        except ValueError:
            print("Invalid number.")
    while True:
        unit_to = input("Enter target unit (w, kw, mw, hp): ").strip().lower()
        result = Power(number, unit_from, unit_to)
        if result is not None:
            print(f"{number} {unit_from} = {round(result, 4)} {unit_to} rounded 4 digits")
            break
        else:
            print("Unsupported unit.")

elif realm == '11':
    print('That\'s Digital Storage section:')
    while True:
        value = input('Input data (e.g., 1 gb): ').strip().split()
        if len(value) != 2:
            continue
        number_str, unit_from = value
        try:
            number = float(number_str)
            break
        except ValueError:
            print("Invalid number.")
    while True:
        unit_to = input("Enter target unit (b, kb, mb, gb, tb): ").strip().lower()
        result = Digital_storage(number, unit_from, unit_to)
        if result is not None:
            print(f"{number} {unit_from} = {round(result, 4)} {unit_to} rounded 4 digits")
            break
        else:
            print("Unsupported unit.")

elif realm == '12':
    print('That\'s Angle section:')
    while True:
        value = input('Input angle (e.g., 180 deg): ').strip().split()
        if len(value) != 2:
            continue
        number_str, unit_from = value
        try:
            number = float(number_str)
            break
        except ValueError:
            print("Invalid number.")
    while True:
        unit_to = input("Enter target unit (deg, rad, grad): ").strip().lower()
        result = Angle(number, unit_from, unit_to)
        if result is not None:
            print(f"{number} {unit_from} = {round(result, 4)} {unit_to} rounded 4 digits")
            break
        else:
            print("Unsupported unit.")