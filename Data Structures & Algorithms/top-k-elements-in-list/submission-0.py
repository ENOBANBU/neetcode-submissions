class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topF = {}
        topA = [[] for i in range(len(nums) + 1)]

        for n in nums:
            topF[n] = 1 + topF.get(n, 0)
        
        for n, c in topF.items():
            topA[c].append(n)

        res = []
        for i in range(len(topA) - 1, 0, -1):
            for n in topA[i]:
                res.append(n)
                if len(res) == k:
                    return res
        