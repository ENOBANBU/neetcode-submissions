class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        curr = 0

        for i in range(len(nums)):
            curr = nums[i]
            for n in range(i+1, len(nums)):
                comp = curr + nums[n]
                if comp == target:
                    return [i, n]   