class Solution:

    def encode(self, strs: List[str]) -> str:
        sti = ""
        for i in strs:
            sti +=  str(len(i)) + "#" + i
        return sti


    def decode(self, s: str) -> List[str]:
        lis = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            leng = int(s[i:j])

            i = j + 1
            lis.append(s[i: i + leng])

            i += leng

        return lis