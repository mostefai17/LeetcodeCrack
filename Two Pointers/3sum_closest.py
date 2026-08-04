class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best_sum = sum(nums[:3])

        for i in range(len(nums) - 2):
            left, right = i+1, len(nums) - 1

            while left < right:
                curr_sum = nums[left] + nums[right] + nums[i]
                
                if curr_sum == target:
                    return target

                elif curr_sum > target:
                    right -= 1
                    
                else:
                    left += 1

                if abs(curr_sum - target) < abs(best_sum - target):
                    best_sum = curr_sum
        return best_sum
