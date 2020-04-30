"""
Given an array of integers, return the four numbers (quadruplets) such that
they add up to a specific given target.

Each input may have multiple solutions

Example:
	arrayOfNums = [7, 6, 4, -1, 1, 2]
	Target = 16
	Solution: [[7, 6, 4, -1], [7, 6, 1, 2]]
"""

# Using the Naive solution which is infact
# the use of four for loops, we would 
# get the time complexity to be O(N^4).
# So, to reduce this complexity we would
# definitely take another approach to solve
# this problem as follows

def fourNumberSum(array, targetSum):
	"""
	Time Complexity: Average => O(N^2)
					 Worst Case => O(N^3) 
	Space Complexity: O(N^2)
	"""
	allPairSums = {}
	quadruplets = []

	for i in range(1, len(array) - 1):
		for j in range(i + 1, len(array)):
			currentSum = array[i] + array[j]
			difference = targetSum - currentSum
			if difference in allPairSums:
				for pair in allPairSums[difference]:
					quadruplets.append(pair + [array[i], array[j]])
		for k in range(0, i):
			currentSum = array[i] + array[k]
			if currentSum not in allPairSums:
				allPairSums[currentSum] = [[array[k], array[i]]]
			else:
				allPairSums[currentSum].append([array[k], array[i]])
	return quadruplets

arrayOfNums = [7, 6, 4, -1, 1, 2]
targetSum = 16
print(f"The quadruplets that adds up to {targetSum} are: {fourNumberSum(arrayOfNums, targetSum)}")