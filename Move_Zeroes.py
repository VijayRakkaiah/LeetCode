class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[a] = nums[a], nums[i]
                a+=1

"""
283. Move Zeroes

PROBLEM:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

"""