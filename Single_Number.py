class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                del d[i]
        single_num = list(d.keys())
        return single_num[0]

'''
136. Single Number

PROBLEM:

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

'''