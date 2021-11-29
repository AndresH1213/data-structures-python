import math
import random

def merge_sort(plist):
	"""
		Sorts a list in ascending order
		Returns a new sorted list

		Divide: Find the midpoint of the list and divide into sublists
		Conquer: Recursively sort the sublists created in previous step
		Combine: Merge the sorted sublists created in previous step
	"""

	if len(plist) <= 1:
		return plist

	left_half, right_half = split(plist)
	left = merge_sort(left_half)
	right = merge_sort(right_half)

	return merge(left, right)

def split(plist):
	"""
		Divide the unsorted lsit at midpoint into sublists
		Returns two sublists - left and right
	"""

	mid = len(plist)//2
	left = plist[:mid]
	right = plist[mid:]

	return left, right

def merge(left, right):
	"""
		Merges two lists (arrays), sorting them in the process
		Returns a new merged list
	"""
	l = []
	i = 0
	j = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			l.append(left[i])
			i += 1
		else:
			l.append(right[j])
			j += 1

	while i < len(left):
		l.append(left[i])
		i += 1

	while j < len(right):
		l.append(right[j])
		j += 1

	return l

alist = [54,62,43,45,34,65,321,65,22,2]

l = merge_sort(alist)

print(l)