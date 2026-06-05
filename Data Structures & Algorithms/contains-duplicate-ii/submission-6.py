class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0,0
        n = len(nums)
        if n - k < 1 :
            return not len(set(nums)) == k
        
        for i in range(n-k):
            count = set(nums[i:i+k+1])
            # print(count)
            if len(count) == k :
                return True

        return False




