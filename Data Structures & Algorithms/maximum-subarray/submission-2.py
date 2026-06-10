class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cur_max = nums[0]
        cur_sum = nums[0]
        for i in range(1,n):
            if cur_sum <= 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            cur_max = max(cur_sum, cur_max)
        return cur_max
