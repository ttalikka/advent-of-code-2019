# -*- coding: utf-8 -*-
"""
Advent of Code Day 7
Amplification Circuit
@ttalikka
"""

from itertools import permutations

def flight_computer(program, *args):
    inputs = []
    for i in args:
        inputs.append(i)
    pos = 0
    L = program
    while True:
        instruction = str(L[pos])[-2:]
       
        if instruction == "99":
            return L[0]
        
        try: 
            opcode_1 = str(L[pos])[-3]
        except:
            opcode_1 = '0'
            
        try:
            opcode_2 = str(L[pos])[-4]
        except:
            opcode_2 = '0'
        
        if instruction == "01" or instruction == "1":
            L[L[pos+3]] = [L[pos+1] if opcode_1 == '1' else L[L[pos+1]]][0] + [L[pos+2] if opcode_2 == '1' else L[L[pos+2]]][0]
            pos += 4
            
        elif instruction == "02" or instruction == "2":
            L[L[pos+3]] = [L[pos+1] if opcode_1 == '1' else L[L[pos+1]]][0] * [L[pos+2] if opcode_2 == '1' else L[L[pos+2]]][0]
            pos += 4
            
        elif instruction == "03" or instruction == "3":
            if inputs:
                L[L[pos+1]] = inputs[0]
                inputs.pop(0)
            elif not inputs:
                L[L[pos+1]] = int(input("Give input\n"))
            pos += 2
            
        elif instruction == "04" or instruction == "4":
            return([L[pos+1] if opcode_1 == '1' else L[L[pos+1]]][0]) 
            #pos += 2
            
        elif instruction == "05" or instruction == "5":
            if [L[pos+1] if opcode_1 == '1' else L[L[pos+1]]][0] != 0:
                pos = [L[pos+2] if opcode_2 == '1' else L[L[pos+2]]][0]
            else:
                pos += 3
                
        elif instruction == "06" or instruction == "6":
            if [L[pos+1] if opcode_1 == '1' else L[L[pos+1]]][0] == 0:
                pos = [L[pos+2] if opcode_2 == '1' else L[L[pos+2]]][0]
            else:
                pos += 3
                
        elif instruction == "07" or instruction == "7":
            if [L[pos+1] if opcode_1 == '1' else L[L[pos+1]]][0] < [L[pos+2] if opcode_2 == '1' else L[L[pos+2]]][0]:
                L[L[pos+3]] = 1
            else:
                L[L[pos+3]] = 0
            pos += 4
                
        elif instruction == "08" or instruction == "8":
            if [L[pos+1] if opcode_1 == '1' else L[L[pos+1]]][0] == [L[pos+2] if opcode_2 == '1' else L[L[pos+2]]][0]:
                L[L[pos+3]] = 1
            else:
                L[L[pos+3]] = 0
            pos += 4
                
        else:
            print("Something went wrong at position {}, trying to interpret instruction {}".format(pos,instruction))
            print(L)
            break

program = [3,8,1001,8,10,8,105,1,0,0,21,38,59,84,93,110,191,272,353,434,99999,3,9,101,5,9,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,4,9,9,1002,9,4,9,4,9,99,3,9,102,5,9,9,1001,9,4,9,1002,9,2,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,4,9,99,3,9,1002,9,5,9,101,4,9,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99]
inputs = list(permutations([n for n in range(5)]))
d = {}
for i in inputs:
    print(i)
    output = 0
    for n in i:
        output = flight_computer(program, n, output)
    print(output)
    d[i] = output

print(sorted(d.items(), key = 
             lambda kv:(kv[1], kv[0]))[-1:]) 
