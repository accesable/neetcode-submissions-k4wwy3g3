class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        c = 0
        n = len(nums)
        while i < n :
            # print(i,n,nums)
            if nums[i] == val :
                self.shrinkElementToLeft(nums,i)
                n -= 1
                continue
            c += 1
            i += 1
        return c
            
                
    def shrinkElementToLeft(self, nums: List[int], index: int) -> None :
        for i in range(index+1, len(nums)):
            nums[i-1] = nums[i]
        