class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        length=len(nums)
        for i in range(0,length):
            value =nums[i]
            difference = target - value
            if value not in d:
                d[difference]=i 
            else:
                previous_index = d[value]
                current_index = i
                output = [previous_index, current_index]
        return output