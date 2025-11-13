def length_converter(value, string_to_what):
    number = float(value[0])
    unit = value[1]

    if unit =='cm':
        if string_to_what == 'm':
            return number /100



print('Type of realms: ',
'\n1 -> Length / Distance' , '2 -> Temperature','3 -> Mass / Weight', '4 -> Volume / Capacity',
'\n5 -> Area', '6 -> Speed / Velocity', '7 -> Time' , '8 -> Energy',
'\n9 -> Pressure', '10 -> Power' , '11 -> Digital Storage / Data',' 12 -> Angle')

print('')

realm = input("What type of converting do you want?(Number please): ")

while not realm.isdigit():
    realm = input("Enter a number please")
    if realm.isdigit():
        continue

if realm == '1':
    print("That's Length/distance-section: ")
    value =input("Input a measurement (metric or US unit, e.g. 24 cm or 10 inches): ").split()
    string_to_what = input('Enter a measurement- metric or US unit, e.g. inches ,ft , inches: ')

    result = length_converter(value, string_to_what)
    if result is not None:
        print(f"{value[0]} {value[1]} = {result} {string_to_what}")