import math

name = input()

L = float(input())
W = float(input())
H = float(input())

print("Hello,", name,".")
print("A square pool using length would contain", ((L*L*H)/7.5), "gallons")
print("A square pool using width would contain", ((W*W*H)/7.5), "gallons")
print("A rectangular pool would contain", ((L*W*H)/7.5), "gallons")
print("A cylindrical pool using length as radius would contain", (.5*math.pi*L*L) , "gallons")
print("A cylindrical pool using width as radius would contain", (.5*math.pi*W*W) , "gallons")