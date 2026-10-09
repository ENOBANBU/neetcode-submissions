class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pair = {}
        curr = 0

        for i in range(len(nums)):
            curr = nums[i]
            comp = target - curr
            if comp in pair:
                return [pair[comp], i]
            pair[nums[i]] = i
        return None
