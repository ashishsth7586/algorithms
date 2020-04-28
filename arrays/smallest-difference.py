"""
Smallest Difference:
Given two arrays of numbers, find the pair of numbers
where one number comes from the first array and another
from the second array with the smallest positive difference.

Example:
array1 = [-1, 5, 10, 20, 28, 3]
array2 = [26, 134, 135, 15, 17]

Smallest Difference: [28, 26]
"""


def smallestDifference(arrayOne, arrayTwo):
	"""
	Time Complexity: nO(logn) + mlog(m)
	where, n is length of array 1
	and m is the length of array 2
	Space Complexity: O(1)
	"""
	arrayOne.sort()
	arrayTwo.sort()

	firstPointer = 0
	secondPointer = 0
	smallest = float("inf")
	current = float("inf")
	smallestPair = []

	while firstPointer < len(arrayOne) and secondPointer < len(arrayTwo):
		firstNum = arrayOne[firstPointer]
		secondNum = arrayTwo[secondPointer]
		if firstNum < secondNum:
			current = secondNum - firstNum
			firstPointer += 1
		elif firstNum > secondNum:
			current = firstNum - secondNum
			secondPointer += 1
		else: 
			return [firstNum, secondNum]
		
		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]
	return smallestPair

array1 = [-1, 5, 10, 20, 28, 3]
array2 = [26, 134, 135, 15, 17]

print(f"The smallest difference is: {smallestDifference(array1, array2)}")