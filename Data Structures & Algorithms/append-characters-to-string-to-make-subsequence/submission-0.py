class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n_s, n_t = len(s), len(t)
        j = 0
        for i in range(n_s) :
            if s[i] == t[j] : 
                j += 1
            if j == n_t :
                break
        return n_t - j