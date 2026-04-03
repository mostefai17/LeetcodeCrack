
# NOTE
# to see the problem visite leetcode.com and search for Move zeros

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0  #Assign a pointer from the left of the array
        for right in range(len(nums)):
          #Here we are looking for the value of the variable right, not it's index, using (right != 0 is a common mistake)
            if nums[right] != 0: 
                nums[left],nums[right] = nums[right], nums[left] #Replacing right value with left value
                left += 1 #When the process is done, we increment (left) and so on
