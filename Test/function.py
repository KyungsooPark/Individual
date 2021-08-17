import math
import calendar

def print_list(a):
    for i in a:
        print(i, len(a))

def add(a, b):
    sum_ab = a + b
    print(str(a) + ' + ' + str(b) + ' = ' + str(sum_ab))
    return a + b


family = ['mother', 'father', 'gentleman', 'sexy lady']
fruits = ['apple','banana','pineapple']

# for x in family:
#     print(x, len(x))

# for x in fruits:
#     print(x, len(x))

print_list(family)
print_list(fruits)

result = add(3, 4)
print(result)

ms = math.sqrt(4)
print(ms)
print(calendar.prmonth(2021, 7))