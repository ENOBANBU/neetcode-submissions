from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_lis = defaultdict(list)
        ans = []

        for i in strs:
            sorted_i = tuple(sorted(i))
            word_lis[sorted_i].append(i)
        
        for val in word_lis.values():
            ans.append(val)
        return ans
            
            