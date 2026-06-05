class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            freq[s[i]] = 1 + freq.get(s[i],0)
            freq[t[i]] = -1 + freq.get(t[i],0)
        
        for i in freq.values():
            if i != 0:
                return False
        return True