# def area_converter(number, unit_from):
#     unit_from = unit_from.lower()
#     if unit_from == 'mm':
#         print(f'{number * number}mm\u00b2')
#         return number * number
#
#     if unit_from == 'cm':
#         print(f'{number *number}cm\u00b2')
#         return number * number
#
#     if unit_from == 'm':
#         print(f'{number *number}m\u00b2')
#         return number * number
#
#     if unit_from == 'km':
#         print(f'{number *number}km\u00b2')
#         return number * number
#     if unit_from == 'yd':
#         print(f'{number *number}yd\u00b2')
#         return number * number
#     if unit_from == 'in':
#         print(f'{number *number}in\u00b2')
#         return number * number
#     if unit_from == 'ft':
#         print(f'{number *number}ft\u00b2')
#         return number * number
#
#
# print("Area:")
# while True:
#     value = input("Input an area (e.g., 150 cm): ").strip().split()
#     if len(value) != 2:
#         print("Invalid format. Try again.")
#         continue
#     number_str, unit_from = value
#     try:
#         number = float(number_str)
#     except ValueError:
#         print("Invalid number. Try again.")
#         continue
#     break
#
# while True:
#     result = area_converter(number, unit_from)
#     if result is not None:
#         result = round(result, 4)
#         print(f"{number} {unit_from} = {result} {unit_from} rounded 4 digits")
#         break
#     else:
#         print("Unsupported unit. Try again.")
#         continue
