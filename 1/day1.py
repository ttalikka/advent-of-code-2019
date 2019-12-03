# -*- coding: utf-8 -*-
"""
Advent of Code Day 1
@ttalikka
"""

from math import floor

def fuelcalc(i):
    return(floor(int(i)/3)-2)

with open("input.txt", "r") as F:
    values = F.read().splitlines()

fuelreq = []

for i in values:
    fuelreq.append(fuelcalc(i))

# Part 1 answer    
print("Sum of fuel requirements:", sum(fuelreq))

fuelreq_addedfuel = []

for i in fuelreq:
    f = i
    totalfuel = i
    while f > 0:
        if fuelcalc(f) <= 0:
            fuelreq_addedfuel.append(totalfuel)
            break
        totalfuel += fuelcalc(f)
        f = fuelcalc(f)
        
# Part 2 answer
print("Sum of fuel requirements with the additional fuel:",sum(fuelreq_addedfuel))
