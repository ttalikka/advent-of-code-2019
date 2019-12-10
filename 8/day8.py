# -*- coding: utf-8 -*-
"""
Advent of Code Day 8
Space Image Format
@ttalikka
"""

import numpy as np

with open("input", "r") as f:
    image = f.read()

# Dimensions
w = 25
h = 6
# Pixels Per Layer
ppl = w*h

i = 0
img_layers = []

while i < len(image):
    img_layers.append(image[i:i+ppl])
    i += ppl

count_zeroes = {}

for i in img_layers:
    count_zeroes[i] = i.count("0")

least_zeroes = sorted(count_zeroes.items(), key = lambda kv:(kv[1], kv[0]))[0][0]
answer_one = least_zeroes.count("1") * least_zeroes.count("2")
print("Answer for part one:",answer_one)

x = np.arange(w*h)
final_image = np.full_like(x,2)

for i in img_layers:
    n = 0
    while n < w*h:
        if final_image[n] == 2:
            final_image[n] = i[n]
        n += 1

pretty_print = np.where(final_image==1,"■","□")
np.set_printoptions(linewidth=np.inf)

print("Answer for part two:\n{}".format(pretty_print.reshape(h,w)))
