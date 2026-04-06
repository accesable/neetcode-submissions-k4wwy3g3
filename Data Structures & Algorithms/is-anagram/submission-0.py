class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = dict()
        if len(s) != len(t) :
            return False
        for i in range(len(s)):
            c = s[i]
            k = t[i]
            if not c in freq :
                freq[c] = 1
            else :
                freq[c] += 1
            if not k in freq:
                freq[k] = -1
            else :
                freq[k] -= 1
        for i in freq.values() :
            if i != 0 :
                return False
        return True