
import random
import math

numbers = [math.ceil(x * random.random()) for x in range(100000)]
def quicksort(values):
	"""
	There are many differents versions of this algorithm
	Picking different elements as the pivot, can be the
	first one, last one or a random element
	"""
	if len(values) <= 1:
		return values
	less_than_pivot = []
	greater_than_pivot = []
	pivot = values[0]
	for value in values[1:]:
		if value <= pivot:
			less_than_pivot.append(value)
		else:
			greater_than_pivot.append(value)
	return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

sorted_numbers = quicksort(numbers)
