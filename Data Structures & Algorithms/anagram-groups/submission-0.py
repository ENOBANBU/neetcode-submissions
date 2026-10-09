from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for i in strs:

            alpcoun = [0] * 26
            for n in i:
                alpcoun[ord(n) - ord('a')] += 1
            ans[tuple(alpcoun)].append(i)
        return list(ans.values())