class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #creating result array
        ans = [1] * len(nums)
        right = 1
        left = 1
        #for loop to loop through left to right algorithm
        for i in range(len(nums)):
            ans[i] = left
            left *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans