# Insert
"""
	linear runtime because all element has
	to shifted forward in the next position
"""
# Appending
"""
	Apending simple add the item to the end so is constant time, but depends on the lenguage. 
	in python there something call Ammortized Constant Space Complexity, when the amount of
	element is near to the space memory that python has assigned to that list increase the memory
	in the append operation, but this means that does not have to do that again until the amount 
	of elements are near to fill the space memory again (resize)
"""
# Extends
"""
	This makes a series of append calls on each of the elements
	of the new list until all of them are appenden to the original
	list, this operation has a run time of O(k) where k is the number of elementes
	in the extend list
"""
numbers = []
numbers.append(2)
numbers.append(200)

numbers.extend([3,5,6])
print(numbers)
# Delente
"""
	Are similar to insert because we need to shift every element to the left and fill the rest of
	the spaces
"""