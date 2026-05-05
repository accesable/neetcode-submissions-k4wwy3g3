class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [0] * n
        suffix_prod = [0] * n
        prefix_prod[0] = nums[0]
        suffix_prod[n-1] = nums[n-1]
        
        for i in range (1,n) :
            prefix_prod[i] = prefix_prod[i-1] * nums[i]
        for i in range (n-2, -1,-1) :
            suffix_prod[i] = suffix_prod[i+1] * nums[i]
        li = []
        for i in range(n) :
            if i == 0 :
                li.append(suffix_prod[i+1])
            elif i == n-1:
                li.append(prefix_prod[i-1])
            else :
                li.append(suffix_prod[i+1] * prefix_prod[i-1])
        return li
