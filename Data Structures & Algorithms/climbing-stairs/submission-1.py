class Solution:
    def climbStairs(self, n: int) -> int:
        one_back = 2
        two_back = 1
        fib_sum = 0

        if n <= 2:
            return n

        for i in range(3, n + 1):
            fib_sum = one_back + two_back
            one_back, two_back = fib_sum, one_back
        return fib_sum
        
