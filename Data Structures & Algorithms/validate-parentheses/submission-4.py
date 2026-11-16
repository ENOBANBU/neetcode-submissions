class Solution:
    def isValid(self, s: str) -> bool:
        hash_brak = {')': '(', '}': '{', ']': '['}
        brak_lis = []

        if len(s) < 2:
            return False
        
        for i in s:
            if i in hash_brak.values():
                brak_lis.append(i)
            elif i in hash_brak:
                if brak_lis and brak_lis.pop() == hash_brak[i]:
                    continue
                else: 
                    return False
        if len(brak_lis) == 0:
            return True
        else:
            return False