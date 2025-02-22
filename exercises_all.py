"""
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
Question 2
Find all the numbers from 1 to 100 (inclusive) that are divisible by any single digit except 1.

For example, 22 is divisible by 2, so it should get included in the result. But 11 is not divisible by any of the digits 2-9, so it should not get included.

Your solution should use comprehensions. (Hint: you may need nested loops in your comprehension)

Next, find all the numbers from 1 to 100 (inclusive) that are not in the list of numbers you just generated.

If your code works correctly, you should end up with this result:

{1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
Question 3
You are given the following data:

data = [
    {'symbol': 'ABCD', 'name': 'ABCD Company', 'ranking': 2, 'risk': 0.2},
    {'symbol': 'BCDE', 'name': 'BCDE Company', 'ranking': 5, 'risk': 0.2},
    {'symbol': 'CDEF', 'name': 'CDEF Company', 'ranking': 8, 'risk': 0.5},
    {'symbol': 'DEFG', 'name': 'DEFG Company', 'ranking': 7, 'risk': 0.8},
    {'symbol': 'EFGH', 'name': 'EFGH Company', 'ranking': 9, 'risk': 0.6},
    {'symbol': 'FGHI', 'name': 'FGHI Company', 'ranking': 10, 'risk': 0.1},
    {'symbol': 'GHIJ', 'name': 'GHIJ Company', 'ranking': 3, 'risk': 0.6},
    {'symbol': 'HIJK', 'name': 'HIJK Company', 'ranking': 5, 'risk': 0.5},
    {'symbol': 'IJKL', 'name': 'IJKL Company', 'ranking': 5, 'risk': 0.7},
    {'symbol': 'JKLM', 'name': 'JKLM Company', 'ranking': 6, 'risk': 0.9},
    {'symbol': 'KLMN', 'name': 'KLMN Company', 'ranking': 6, 'risk': 0.4},
    {'symbol': 'LMNO', 'name': 'LMNO Company', 'ranking': 8, 'risk': 0.4},
    {'symbol': 'MNOP', 'name': 'MNOP Company', 'ranking': 8, 'risk': 0.2},
    {'symbol': 'NOPQ', 'name': 'NOPQ Company', 'ranking': 1, 'risk': 0.5},
    {'symbol': 'OPQR', 'name': 'OPQR Company', 'ranking': 9, 'risk': 0.2},
    {'symbol': 'PQRS', 'name': 'PQRS Company', 'ranking': 10, 'risk': 0.9},
    {'symbol': 'QRST', 'name': 'QRST Company', 'ranking': 3, 'risk': 0.4},
    {'symbol': 'RSTU', 'name': 'RSTU Company', 'ranking': 7, 'risk': 0.3},
    {'symbol': 'STUV', 'name': 'STUV Company', 'ranking': 8, 'risk': 0.1},
    {'symbol': 'TUVW', 'name': 'TUVW Company', 'ranking': 7, 'risk': 0.9}
]
Write code that does these two things:

creates a new list of of dictionaries where the ranking is at least 5, and the risk is less than 0.6
these dictionaries should contain the symbol and a calculated key, named weighted, which is the result of dividing ranking by risk. (You should round this value two decimal places). Do not mutate the original data list or dictionaries in any way.
"""