class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for n in range(len(digits) - 1, -1, -1):
            if digits[n] < 9:
                digits[n] += 1
                return digits
            elif digits[n] >= 9:
                digits[n] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
        