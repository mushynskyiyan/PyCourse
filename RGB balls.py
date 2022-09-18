'''
A drawer contains marbles of three different colors, red, blue and green, given the amounts of each color of marble,
if three marbles are selected at random, figure out the probability (as a percentage, rounded down), that there will be
one of each color in the selection.
The probability of selecting one marble of each color as a percentage (rounded down) outputted as a string
'''

import math

r = int(input("Red balls: "))
b = int(input("Blue balls: "))
g = int(input("Green balls: "))
probr = r/(r+b+g)
probb = b/((r-1)+b+g)
probg = g/((r-1)+(b-1)+g)
prob = (probr * probb * probg) * 100 * 6
pro = math.floor(prob)
print(f"{pro}%")