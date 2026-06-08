class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        n = len(arr)
        max_element = -1
        for i in range(n-1,-1,-1) :
            pre_max = max_element
            max_element = max(arr[i],max_element)
            arr[i] = pre_max
        return arr

