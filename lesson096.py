widget_sales = [
    {'name': 'widget 1', 'sales': 10},
    {'name': 'widget 2', 'sales': 5},
    {'name': 'widget 3', 'sales': 0},
]

sales_by_widget = {}
for d in widget_sales:
    widget_name = d['name']
    sales = d['sales']
    sales_by_widget[widget_name] = sales
print(sales_by_widget)
print()

sales_by_widget = {}
for d in widget_sales:
    sales_by_widget[d['name']] = d['sales']
print(sales_by_widget)
print()

sales_by_widget = {d['name']: d['sales'] for d in widget_sales}
print(sales_by_widget)
print('-'*80)

sales_by_widget = {}
for d in widget_sales:
    if d['sales'] > 0:
        sales_by_widget[d['name']] = d['sales']
print(sales_by_widget)
print()

sales_by_widget = {d['name']: d['sales'] for d in widget_sales if d['sales'] > 0}
print(sales_by_widget)
print('-'*80)


punctuation = ",.!:-\n"
paragraph = """
To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to.
"""

for char in punctuation:
    paragraph = paragraph.replace(char, ' ')

print(paragraph)
all_words = paragraph.split()
print(all_words)
words = {word.lower() for word in all_words if len(word) > 4}
print(words)
print('='*80)

data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd' ]
freq = {}
for element in set(data):
    count = len([char for char in data if char == element])
    freq[element] = count
print(freq)
print()

freq = {
    element: len([char for char in data if char == element])
    for element in set(data)
}
print(freq)
print()
print('-'*80)

from collections import Counter
data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd' ]
freq = Counter(data)
print(freq)
print(dict(freq))
print('='*80)

paragraph = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure 
dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum."""
freq = Counter(paragraph)
print(dict(freq))
print()

ignored = " ,.\n"
freq = Counter(paragraph.casefold())
print(freq)
freq = {key: value for key, value in freq.items() if key not in ignored}
print(freq)
print('-'*80)


freq = {
    key: value
    for key, value in dict(Counter(paragraph.casefold())).items()
    if key not in ignored
}
print(freq)
print()

freq = {
    key: value
    for key, value in Counter(paragraph.casefold()).items()
    if key not in ignored
}
print(freq)
print()


