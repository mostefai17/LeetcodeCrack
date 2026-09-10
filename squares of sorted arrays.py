class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0 
        right = len(nums) 
        result = [] 
        while left < right: 
            if left ** 2 < right ** 2:
                result.append(nums[left] ** 2)
                left += 1 
            else: 
                result.append(nums[right] ** 2)
                right -= 1 
                
        result.sort()
        
        return result
