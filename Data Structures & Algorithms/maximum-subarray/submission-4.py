class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cur_max = nums[0]
        cur_sum = nums[0]
        for i in range(1,n):
            cur_sum += nums[i]
            if cur_sum < nums[i]:
                cur_sum = nums[i]
            cur_max = max(cur_max, cur_sum)
        return cur_max
