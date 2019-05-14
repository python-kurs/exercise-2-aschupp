# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500
               }

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]

sat_database["GOES"]=2000
sat_database["worldview"]=0.31

print("I have the following satellites in my database:")
print(sat_database)

# 2) print out all satellite names contained in the dictionary [2P]

print (sat_database.keys ())

# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]

a = input("For informations about the resolution, please enter satellites name") 

print(sat_database.get(a))

# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]

if a == True:
            print("satellite found in database")
else:
            print("satellite does not exist")
            
#OR
            
if a in sat_database:
        print("satellite found in database")
else:
        print("satellite does not exist")

# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P]
            
if a == "METEOSAT":
    print("The resolution is 3000 m")
elif a == "LANDSAT":
    print("The resolution is 30 m")
elif a == "MODIS":
    print("The resolution is 500 m")
elif a == "GOES":
    print("The resolution is 2000 m")
elif a == "worldview": 
    print("The resolution is 0.31 m")
else:
    print("Satellite not found")               