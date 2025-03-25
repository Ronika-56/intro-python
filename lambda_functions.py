# lambda_functions
from functools import reduce


def add_two_numbers(a, b):
    return a + b



print(add_two_numbers(2, 17))

add_two =lambda a, b: a + b

print(add_two(1, 2))

scores =[ {"Bio": 80 , "Business": 90 } ,
          {"Bio": 64 , "Business": 56 } ,
          {"Bio": 50 , "Business": 78 } ,
          {"Bio": 28, "Business": 46 }]

sorted_by_maths =sorted(scores, key=lambda s: s["Bio"])
print(sorted_by_maths)

def get_Bio_score(score):
    return score["Business"]

sorted_by_biology =sorted(scores, key=get_Bio_score)
print(sorted_by_biology)

ages = [ 18 ,19 ,23 ,25,56,34,45,67,70,80]
total_age = reduce( lambda x, y: x + y, ages)
print(total_age)

new_age =map(lambda x : x / x+1, ages)
print(list(new_age))

above_30 =filter(lambda age : age > 30, ages)























