class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        n = len(nums)
        con = set()
        # if k == 0 :
        #     return False
        for R in range(n):
            if abs(R - L) > k :
                con.remove(nums[L])
                L += 1
            if nums[R] in con :
                return True
            con.add(nums[R])
        return False