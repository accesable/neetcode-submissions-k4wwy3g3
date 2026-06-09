class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = 0
        cur_max = 0
        for i in nums:
            if i == 1 :
                cur += 1
            else :
                cur = 0
            cur_max = max(cur_max,cur)
                
        return cur_max