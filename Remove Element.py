class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Keys To solve this problem
# Keep one pointer/index for the next write position (i)
# Iterate input with another read pointer (for num in nums)
# Overwrite nums[i] with valid values (num != val)
# Increment i
# Return i as new length

        i = 0 #Setting i as the pointer
        for num in nums: 
            if num != val: 
                nums[i] = num
                i += 1
        return i
