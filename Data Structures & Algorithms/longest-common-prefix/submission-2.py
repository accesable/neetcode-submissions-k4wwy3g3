class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        i = 0
        lowest = len(strs[0])
        for s in strs:
            lowest = min(lowest, len(s))
        
        while i < lowest:
            cur_char = strs[0][i]
            for s in strs:
                if s[i] != cur_char:
                    return pre
            pre += cur_char
            i += 1
        
        return pre