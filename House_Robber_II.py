class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
            
        def robber(nums):
            if len(nums) == 0:
                return 0
            elif len(nums) == 1:
                return nums[0]
            elif len(nums) == 2:
                return max(nums[0], nums[1])
            else:
                dp = [0] * len(nums)
                dp[0] = nums[0]
                dp[1] = max(nums[0], nums[1])
                for i in range(2, len(nums)):
                    current_house_rob = nums[i] + dp[i-2]
                    dp[i] = max(current_house_rob, dp[i-1])
                return dp[-1]

        nums_1 = nums[:len(nums)-1]
        nums_2 = nums[1:]

        result_1 = robber(nums_1)
        result_2 = robber(nums_2)

        return max(result_1, result_2)
            
 """
213. House Robber II
 
PROBLEM: 
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
 """