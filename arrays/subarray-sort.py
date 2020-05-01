# !/usr/bin/python3
# Problem: To find the indices smallest sub array such 
# that the entire input array is sorted.

# Example:
# array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
# The starting and ending index of sub array is [3, 9]
# which is not sorted. So after sorting this sub array,
# the entire input array is sorted.

# Steps:
# 1. Loop through each number in a given input array,
#    compare each number with its adjacent numbers
#    to make sure that it is properly sorted.
#    i.e. In above example, all the numbers except 
#    11, 7,12 and 6 is properly sorted.
# 2. Now, we find the smallest and largest number in
#    the obtained unsorted numbers and then look
#    the final sorted position of those numbers in 
#    the final array. Based on this, we can find 
#    the indices from which we should sort the sub array.
#    As from above scenario, 6 is gonna be in 3rd indices
#    and for 12, its gonna be in 9th position.
# 3. Now we place 6 and 12 to its respective indices and
#    then we sort the other numbers between 6 and 12.
#    As a result, we get the entire array sorted.
#

def subarraySort(array):
	"""
	Time Complexity: O(N)
	Space Complexity: O(1)
	"""
	minOutOfOrder = float("inf")
	maxOutOfOrder = float("-inf")
	for i in range(len(array)):
		num = array[i]
		if isOutOfOrder(i, num, array):
			minOutOfOrder = min(minOutOfOrder, num)
			maxOutOfOrder = max(maxOutOfOrder, num)
	
	if minOutOfOrder == float("inf"):
		return [-1, -1]

	subarrayLeftIndex = 0
	while minOutOfOrder >= array[subarrayLeftIndex]:
		subarrayLeftIndex += 1
	subarrayRighIndex = len(array) - 1
	while maxOutOfOrder <= array[subarrayRighIndex]:
		subarrayRighIndex -= 1
	return [subarrayLeftIndex, subarrayRighIndex]


def isOutOfOrder(i, num, array):
	if i == 0:
		return num > array[i + 1]
	if i == len(array) - 1:
		return num < array[i - 1]
	return num > array[i + 1] or num < array[i - 1]

array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(f"The indices of smallest unsorted array is: {subarraySort(array)}")