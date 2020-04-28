"""
WAP to move element to end of an array.

Example:
Given,
array = [2, 1, 2, 2, 2, 3, 4, 2]
Element to put to end => 2
Result = [1, 3, 4, 2, 2, 2, 2, 2]
"""

def moveElementToEnd(array, numToMove):
	"""
	Time Complexity: O(n)
	Space Complexity: O(1)
	"""
	i = 0
	j = len(array) - 1

	while i < j:
		while i < j and array[j] == numToMove:
			j -= 1
		if array[i] == numToMove:
			array[i], array[j] = array[j], array[i]
		i += 1
	return array

array = [2, 1, 2, 2, 2, 3, 4, 2]
numToMove = 2
print(f"After moving {numToMove}, the array becomes: {moveElementToEnd(array, numToMove)}")



