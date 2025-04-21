set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
union_set = set_a.union(set_b)
print("Union:", union_set)

intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)

difference_set = set_a.difference(set_b)
print("Difference:", difference_set)

symmetric_diff_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", symmetric_diff_set)

set_a.add(7)  # Add an element to set_a
print("After adding 7 to set_a:", set_a)

set_b.remove(5)  # Remove an element from set_b
print("After removing 5 from set_b:", set_b)
