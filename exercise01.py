'''
Question 1
Given the following data:

data = [
    {'open': 100, 'high': 120, 'low': 90, 'close': 110},
    {'open': 110, 'high': 130, 'low': 80, 'close': 120},
    {'open': 120, 'high': 140, 'low': 70, 'close': 130},
    {'open': 130, 'high': 150, 'low': 60, 'close': 140},
]
Re-write the following code using a comprehension:

ranges = []
for d in data:
    ranges.append(d['high'] - d['low'])
'''
