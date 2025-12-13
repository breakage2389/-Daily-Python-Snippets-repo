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

    if unit_from not in to_liters or unit_to not in to_liters:
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
