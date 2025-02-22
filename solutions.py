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
Solution
Instead of using a loop to iteratively append elements to an empty list, we can define the list directly using a comprehension:

ranges = [d['high'] - d['low'] for d in data]
ranges
[30, 50, 70, 90]
Question 2
Find all the numbers from 1 to 100 (inclusive) that are divisible by any single digit except 1.

For example, 22 is divisible by 2, so it should get included in the result. But 11 is not divisible by any of the digits 2-9, so it should not get included.

Your solution should use comprehensions. (Hint: you may need nested loops in your comprehension)

Next, find all the numbers from 1 to 100 (inclusive) that are not in the list of numbers you just generated.

If your code works correctly, you should end up with this result:

{1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
Solution
Let's solve this using a non-comprehension first to get a feel for the algorithm.

result = []

for number in range(1, 101):
    for n in range(2, 10):
        if number % n == 0:
            result.append(number)
            break  # no need to try other divisors, so exit inner loop early

print(result)
[2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100]
not_divisible = set(range(1, 100)) - set(result)
print(not_divisible)
{1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
Now let's try a comprehension approach to find the list of divisible numbers:

result = [number for number in range(1, 101) for n in range(2, 10) if number % n == 0]
print(result)
[2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 8, 8, 9, 9, 10, 10, 12, 12, 12, 12, 14, 14, 15, 15, 16, 16, 16, 18, 18, 18, 18, 20, 20, 20, 21, 21, 22, 24, 24, 24, 24, 24, 25, 26, 27, 27, 28, 28, 28, 30, 30, 30, 30, 32, 32, 32, 33, 34, 35, 35, 36, 36, 36, 36, 36, 38, 39, 40, 40, 40, 40, 42, 42, 42, 42, 44, 44, 45, 45, 45, 46, 48, 48, 48, 48, 48, 49, 50, 50, 51, 52, 52, 54, 54, 54, 54, 55, 56, 56, 56, 56, 57, 58, 60, 60, 60, 60, 60, 62, 63, 63, 63, 64, 64, 64, 65, 66, 66, 66, 68, 68, 69, 70, 70, 70, 72, 72, 72, 72, 72, 72, 74, 75, 75, 76, 76, 77, 78, 78, 78, 80, 80, 80, 80, 81, 81, 82, 84, 84, 84, 84, 84, 85, 86, 87, 88, 88, 88, 90, 90, 90, 90, 90, 91, 92, 92, 93, 94, 95, 96, 96, 96, 96, 96, 98, 98, 99, 99, 100, 100, 100]
As you can see we have repeated results (because a number may be divisible by multiple single digit numbers). We were able to circumvent this problem in our first approach by breaking out of the inner loop, but we don't have that control in a comprehension.

However, we can easily rectify this by making a set out of those numbers, using a set comprehension:

result = {number for number in range(1, 101) for n in range(2, 10) if number % n == 0}
print(result)
{2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100}
Now that we have this result, we can proceed just as before using set subtraction to get the list of non-divisible numbers:

result = set(range(1, 101)) - result
print(result)
{1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
You might be wondering if maybe the first approach, although not as elegant as a comprehension might actually run faster given that we break out of the inner loop early.

We will perform less calculations using the first approach, so we probably shoudl expect it to run faster.

Let's time things and see.

from time import perf_counter
start_time = perf_counter()
result = []

for number in range(1, 101):
    for n in range(2, 10):
        if number % n == 0:
            result.append(number)
            break  # no need to try other divisors, so exit inner loop early

end_time = perf_counter()
print(end_time - start_time, "seconds elapsed")
6.895797559991479e-05 seconds elapsed
Now, let's do the same timing, but using the comprehension:

start_time = perf_counter()
result = {number for number in range(1, 101) for n in range(2, 10) if number % n == 0}
end_time = perf_counter()
print(end_time - start_time, "seconds elapsed")
6.987503729760647e-05 seconds elapsed
The timings seem quite close to each other, but what happens if we run this for a much larger set of numbers?

start_time = perf_counter()
result = []

for number in range(1, 1_000_000):
    for n in range(2, 10):
        if number % n == 0:
            result.append(number)
            break  # no need to try other divisors, so exit inner loop early

end_time = perf_counter()
print(end_time - start_time, "seconds elapsed")
0.2512881669681519 seconds elapsed
start_time = perf_counter()
result = {number for number in range(1, 1_000_000) for n in range(2, 10) if number % n == 0}
end_time = perf_counter()
print(end_time - start_time, "seconds elapsed")
0.3111054169712588 seconds elapsed
As you can see, the comprehension approach actually gets slower as we deal with more and more numbers.

The moral of the story here is that a comprehension is not always more efficient than the standard loop/append we did first. And that's because we were able to cut out calculations in the loop/append approach that we were unable to do using a comprehension.

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
Solution
We can use a list comprehension directly, using the optional if part of the comprehension for filtering the rows we want:

result = [d for d in data if d['ranking'] >= 6 and d['risk'] < 0.6]
result
[{'symbol': 'CDEF', 'name': 'CDEF Company', 'ranking': 8, 'risk': 0.5},
 {'symbol': 'FGHI', 'name': 'FGHI Company', 'ranking': 10, 'risk': 0.1},
 {'symbol': 'KLMN', 'name': 'KLMN Company', 'ranking': 6, 'risk': 0.4},
 {'symbol': 'LMNO', 'name': 'LMNO Company', 'ranking': 8, 'risk': 0.4},
 {'symbol': 'MNOP', 'name': 'MNOP Company', 'ranking': 8, 'risk': 0.2},
 {'symbol': 'OPQR', 'name': 'OPQR Company', 'ranking': 9, 'risk': 0.2},
 {'symbol': 'RSTU', 'name': 'RSTU Company', 'ranking': 7, 'risk': 0.3},
 {'symbol': 'STUV', 'name': 'STUV Company', 'ranking': 8, 'risk': 0.1}]
So this approach gets almost all the way to our solution. However, we do not want the original dictionaries here, but just the symbol and the calculated weighted value.

We can very simply modify our original comprehension this way:

result = [
    {
        'symbol': d['symbol'],
        'weighted': round(d['ranking'] / d['risk'], 2)
    }
    for d in data
    if d['ranking'] >= 5 and d['risk'] < 0.6
]
result
[{'symbol': 'BCDE', 'weighted': 25.0},
 {'symbol': 'CDEF', 'weighted': 16.0},
 {'symbol': 'FGHI', 'weighted': 100.0},
 {'symbol': 'HIJK', 'weighted': 10.0},
 {'symbol': 'KLMN', 'weighted': 15.0},
 {'symbol': 'LMNO', 'weighted': 20.0},
 {'symbol': 'MNOP', 'weighted': 40.0},
 {'symbol': 'OPQR', 'weighted': 45.0},
 {'symbol': 'RSTU', 'weighted': 23.33},
 {'symbol': 'STUV', 'weighted': 80.0}]
"""