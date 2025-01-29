# Create a set
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)

# Add an element
fruits.add("orange")
print("After adding 'orange':", fruits)

# Remove an element
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Check for membership
is_in_set = "apple" in fruits
print("Is 'apple' in the set?", is_in_set)

# Perform set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print("Union of sets:", set1.union(set2))

# Intersection
print("Intersection of sets:", set1.intersection(set2))

# Difference
print("Difference of sets (set1 - set2):", set1.difference(set2))

# Symmetric Difference
print("Symmetric difference of sets:", set1.symmetric_difference(set2))
