class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = sum(arr[:k])
        counter = 0

        if k > len(arr):
            pass

        # compare first before iterating to avoid edge case
        if window  >= threshold * k:
            counter += 1

        for i in range(k, len(arr)):
            window += arr[i] - arr[i-k]

            if window >= threshold * k:
                counter += 1
            else:
                pass
        
        return counter
