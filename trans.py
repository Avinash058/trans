print("--------------------------------------------")
print("-------------Transport App------------------")
print("--------------------------------------------")
location = {"Dwaraka Nagar":0,"Beach Road":5,"Gajuwaka":25,"Madurawada":20}
loc = {1:"Dwaraka Nagar",2:"Beach Road",3:"Gajuwaka",4:"Madurawada"}
modeof = {1:"Bus",2:"Car",3:"Auto",4:"Cab"}
minimumfare = {1:10,2:20,3:5,4:7}
costperkm = {1:2,2:10,3:3,4:4}
time = {1:50,2:80,3:30,4:40}
while True:
    try:
        start = int(input("""
        Enter your location:
            1) Dwaraka nagar -1
            2) Beach Road    -2
            3) Gajuwaka      -3
            4) Madurawada    -4
            Ex: enter "1" for Dwaraka nagar
            """))
        if not 1<=start<=4:
            print()
            print("Enter Valid location number between 1 and 4")
        else:
            end = int(input("""
        Enter your destination:
            1) Dwaraka nagar -1
            2) Beach Road    -2
            3) Gajuwaka      -3
            4) Madurawada    -4
            Ex: enter "1" for Dwaraka nagar
            """))
            if not 1<=end<=4:
                print()
                print("Enter Valid location number between 1 and 4")
            else:
                break
    except:
        print("Enter a Valid numerical input")
while True:
    try:
        mode = int(input("""Select mode of Transportation:
    1 - Bus
    2 - Car
    3 - Auto
    4 - Cab
     """))
        if not 1<=mode<=4:
            print("Enter valid mode of transportation between 1 and 4")
        else:
            break
    except:
        print("Enter a Valid numerical input")
print("-------------------------------------------------")
print("-------------------------------------------------")
print()
dist = location[loc[start]]+location[loc[end]]
if start==end:
    print("Start and Destination Locations are Same")
else:
    print(f"""The total distance from {loc[start]} to {loc[end]} is : {dist}
Cost for {modeof[mode]}:{minimumfare[mode]+(dist*costperkm[mode])}
 Estimated total time: {dist/time[mode]}
""")
        
