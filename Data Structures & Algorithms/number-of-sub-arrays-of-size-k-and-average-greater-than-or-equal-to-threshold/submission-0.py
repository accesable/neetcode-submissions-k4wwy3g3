class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = set()
        L = 0
        count = 0
        n = len(arr)
        cur_avg = 0
        if n < k:
            return 0

        for R in range(n):
            cur_avg += arr[R]
            x = R - L + 1
            if x == k and (cur_avg // k >= threshold):
                count += 1
                cur_avg -= arr[L]
                L += 1
            elif x == k:
                cur_avg -= arr[L]
                L += 1

        return count
