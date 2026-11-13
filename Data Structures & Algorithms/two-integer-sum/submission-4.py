class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pair = {}
        curr = 0

        for n in range(len(nums)):
            curr = target - nums[n]
            if curr in pair:
                return [pair[curr], n]
            pair[nums[n]] = n
        return None