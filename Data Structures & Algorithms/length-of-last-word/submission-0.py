class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strs = s.split()
        print(strs)
        return len(strs[-1])