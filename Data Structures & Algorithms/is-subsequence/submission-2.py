class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        n_s = len(s)
        n_t = len(t)
        if n_s == 0 :
            return True
        if n_t == 0 :
            return False
        for i in range(n_t):
            if s[j] == t[i]:
                j += 1
            if j == n_s:
                return True
            
        return j == n_s 
