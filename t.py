my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

single_element_tuple = (5,)
print(type(single_element_tuple))

print(my_tuple[0])  
print(my_tuple[-1])

print(my_tuple[1:4])

for item in my_tuple:
    print(item)

print(len(my_tuple))


tuple1 = (1, 2)
tuple2 = (3, 4)
tuple3 = tuple1 + tuple2
print(tuple3)

sample = (1, 2, 2, 3, 4)

print(sample.count(2))  # Output: 2
print(sample.index(3))  # Output: 3

a, b, c, d, e = my_tuple
print(a) 

