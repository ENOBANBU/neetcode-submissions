class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        if s == t:
            return True

        letters = {}

        for i in range(len(s)):
            if s[i] not in letters:
                letters[s[i]] = 1
            else:
                letters[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in letters:
                return False
            letters[t[i]] -= 1
            if letters[t[i]] < 0:
                return False
            
        return True
        
        

        


