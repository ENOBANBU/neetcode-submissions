class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_back = 0
        two_back = 0
        tot_min = 0

        for i in range(len(cost) - 1, -1, -1):
            curr = cost[i] + min(one_back, two_back)
            two_back, one_back = one_back, curr
            tot_min = min(one_back, two_back)
        return tot_min