class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        mid = 0
        while l <= r :
            mid = ((r - l) // 2) + l
            if nums[mid] > target :
                r = mid - 1
            elif nums[mid] < target : 
                l = mid + 1
            else :
                return mid
        
        return -1