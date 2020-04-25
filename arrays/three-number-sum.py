"""
Given an array of integers, return the three numbers such that
they add up to a specific given target.

Each input may have multiple solutions

Example:
	arrayOfNums = [12, 3, 1, 2, -6, 5, -8, 6]
	target = 0
	Result = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""

nums = [12,  3, 1, 2, -6, 5, -8, 6]
targetSum = 0

def threeNumberSum_loops(nums, targetSum):
	"""
	Using conventional three for loops.
	Time Complexity: O(n^3)
	Space Complexity: O(n)
	"""
	triplets = []
	for i in range(len(nums) - 2):
		firstNum = nums[i]
		for j in range(i + 1, len(nums)):
			secondNum = nums[j]
			for k in range(j + 1, len(nums)):
				thirdNum = nums[k]
				if firstNum + secondNum + thirdNum == targetSum:
					 triplets.append([firstNum, secondNum, thirdNum])
	return triplets

def threeNumberSum_sort(nums, targetSum):
	"""
	The time complexity obtained above can be reduced to
	O(n^2) by using Sorting.
	Space Complexity: O(n)
	"""
	nums.sort()
	triplets = []
	for i in range(len(nums) - 2):
		left = i + 1
		right = len(nums) - 1
		while left < right:
			currentSum = nums[i] + nums[left] + nums[right]
			if currentSum == targetSum:
				triplets.append([nums[i], nums[left], nums[right]])
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left += 1
			elif currentSum > targetSum:
				right -= 1
	return triplets



print(f"The three numbers that equals {targetSum} is {threeNumberSum_loops(nums, targetSum)}")
print(f"The three numbers that equals {targetSum} is {threeNumberSum_sort(nums, targetSum)}")