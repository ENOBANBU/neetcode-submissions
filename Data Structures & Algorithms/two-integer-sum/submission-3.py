class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pair = {}
        comp = 0

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in pair:
                return [pair[comp], i]
            pair[nums[i]] = i
        return None        
