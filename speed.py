def Speed_converter(number , unit_from , unit_to):
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
        if unit_to == "m/s": return (number *1.609)/3.6

    return None