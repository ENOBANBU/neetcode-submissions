class Solution:
    def isHappy(self, n: int) -> bool:
        self.sum_ = 0
        dups = set()
        boolo = True

        def math(num: int):
            curr_sum = 0
            for i in str(num):
                curr_sum += int(i) ** 2
            return curr_sum

        self.sum_ = math(n)
        while 1 not in dups:
            if self.sum_ not in dups:
                dups.add(self.sum_)
                self.sum_ = math(self.sum_)
            else:
                return False
        return True