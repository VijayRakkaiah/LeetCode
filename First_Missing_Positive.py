class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            positive = abs(nums[i])
            if positive >= 1 and positive <= len(nums):
                actual = positive - 1
                if nums[actual] == 0:
                    nums[actual] = -1 * (len(nums)+1)
                elif nums[actual] > 0:
                    nums[actual] = nums[actual] * -1
        
        for i in range(len(nums)):
            if nums[i] < 0:
                continue
            elif nums[i] >= 0:
                return i+1
        
        return len(nums)+1
            
 """
41. First Missing Positive
 
PROBLEM: 
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 """