class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = best = sum([:k])

        for r in range(len(k,nums)):
            curr = curr + nums[r] - nums[r-k]

            best = max(best,curr)

        return best / k
