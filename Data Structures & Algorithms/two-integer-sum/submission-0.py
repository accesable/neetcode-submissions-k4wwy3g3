class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = dict()
        for i in range(len(nums)) :
            if nums[i] in remainder :
                return [remainder[nums[i]],i]
            else :
                remainder[target - nums[i]] = i
        return [0,0]
        