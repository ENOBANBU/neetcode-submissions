class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for word in strs:
            sorted_w = ("".join(sorted(word)))

            if sorted_w not in ans:
                ans[sorted_w] = []
            ans[sorted_w].append(word)
        return list(ans.values())
            