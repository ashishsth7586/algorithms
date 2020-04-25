"""
Given an array of integers, return the two numbers such that
they add up to a specific given target.

Assume that each input would have exactly one solution, and same element
is not used.

Example:
	arrayOfNums = [-1, 3, 11, 2, 7]
	target = 9
	Result = [2, 7]
"""

# Solution 1: Using Two for loops
# O(n^2) | O(1) Space
def twoNumberSum_forLoops (nums, targetSum):
	for i in range(len(nums) - 1):
		firstNum = nums[i]
		for j in range(i + 1, len(nums)):
			secondNum = nums[j]
			if firstNum + secondNum == targetSum:
				return [firstNum, secondNum]
	return []

# Solution 2: Using Hash Table
# O(n) Time | O(n) Space
def twoNumberSum_hashTable(nums, targetSum):
	hash_nums = {}
	for num in nums:
		potentialMatch = targetSum - num
		if potentialMatch in hash_nums:
			return [potentialMatch, num]
		else:
			hash_nums[num] = True
	return []

# Solution 3: Using Sorting algorithm
# and traversing the array using the computed sum
# O(nlogn) Time | O(1) Space
def twoNumberSum_sort(nums, targetSum):
	nums.sort()
	left = 0
	right = len(nums) - 1
	while left < right:
		currentSum = nums[left] + nums[right]
		if currentSum == targetSum:
			return [nums[left], nums[right]]
		elif currentSum < targetSum:
			left += 1
		elif currentSum > targetSum:
			right -= 1
	return []


# In above methods for implementing the Two Sum Problem
# we saw that using one among three has their own trade-off
# for time and space complexity. 
# Solution 1 is considered as the worst case since time and
# space complexity is more than other two solutions.
# Whether we require less time complexity or less space 
# complexity, we need to choose either Solution 1 or Solution 2.

nums = [-1, -11, 3, 11, 2, 7]
targetSum = 9
print(f"The array of numbers is: {nums}")
print(f"The target sum is: {targetSum}")
print(f"Using Solution 1: {twoNumberSum_forLoops(nums, targetSum)}")
print(f"Using Solution 2: {twoNumberSum_hashTable(nums, targetSum)}")
print(f"Using Solution 3: {twoNumberSum_sort(nums, targetSum)}")