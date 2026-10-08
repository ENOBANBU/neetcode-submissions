class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()

        if len(nums) == 0 or len(nums) == 1:
            return False

        for i in range(len(nums)):
            if nums[i] not in dup:
                dup.add(nums[i])
            elif nums[i] in dup:
                return True
        return False