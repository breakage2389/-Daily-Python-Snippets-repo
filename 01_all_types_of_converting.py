# def length_converter(n, m):



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
