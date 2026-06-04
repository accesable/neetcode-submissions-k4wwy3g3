class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority_n = len(nums) / 2
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i,0)
            if freq[i] > majority_n :
                return i
        return 0