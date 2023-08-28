import re

pattern = re.compile("[0-9A-Za-z]+")

ans = pattern.finditer("你好")
for t in ans:
    print(t.group())


import pandas as pd


import math
import numpy as np

a = [0.8, 0.15, 0.5]
b = [1, -0.13, 0.4]

vec1 = np.array(a)
vec2 = np.array(b)

cos_sim = vec1.dot(vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
print(cos_sim)

s = "abc"
s = s.__add__("f")
print(s)