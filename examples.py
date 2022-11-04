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

# Flatten list
a = [1 ,2, 3, 4, [12, 13, 14], 15, 16, 17, [18], [19, [20]]]
flattened = Pystream(a).flat(num_levels=2).collect()
print(flattened)

# Duplicate all elements
a = [1,2,3,4,5]
duplicated = Pystream(a, True).flatmap(lambda x: [x, x]).collect()
print(duplicated)

# Print all elements in a list
Pystream(lst).foreach(lambda x: print(x))
