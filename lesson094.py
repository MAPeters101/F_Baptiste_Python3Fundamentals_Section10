
vectors = [(0,0), (0,1), (1,0), (1,1)]
from math import sqrt

magnitudes = []
for vector in vectors:
    magnitude = sqrt(vector[0]**2 + vector[1]**2)
    magnitudes.append(magnitude)
print(magnitudes)
print('-'*80)

magnitudes = [sqrt(vector[0]**2 + vector[1]**2) for vector in vectors]
print(magnitudes)
print('-'*80)

