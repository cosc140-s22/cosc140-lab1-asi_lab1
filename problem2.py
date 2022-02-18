#
# Name:Matt/Asianna
# Collaborator(s):
#
import math

Lat_place1 = math.radians(float(input("What is the Latitude? ")))
Long_place1 = math.radians(float(input("What is the longitude? ")))
Lat_place2 = math.radians(float(input("What is the Latitude? ")))
Long_place2 = math.radians(float(input("What is the longitude? ")))

dlon = Long_place2 - Long_place1
dlat = Lat_place2 - Lat_place1
a = (math.sin(dlat/2))**2 + math.cos(Lat_place1) * math.cos(Lat_place2) * (math.sin(dlon/2))**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
D = 3956 * c

print(D)
print(f"{Lat_place1},{Long_place1}one and {Lat_place2}, {Long_place2} two have a Haversine distance of {D}")