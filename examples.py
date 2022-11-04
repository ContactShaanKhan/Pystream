from pystream import Pystream

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Filter even values
evens = Pystream(lst, default_in_place=True).filter(lambda x: x % 2 == 0).collect()
print(evens)

# Filter evens and multiply by 10
def is_even(x):
    return x % 2 == 0

ten_times_even = Pystream(lst).filter(is_even).map(lambda x: x * 10).collect()
print(ten_times_even)

# Reduce list for sum
sum_of_lst = Pystream(lst, True).reduce(lambda x, y: x + y).collect()
print(sum_of_lst)
