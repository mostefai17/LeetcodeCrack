class Solution:
    def isPalindrome(self, x: int) -> bool:
        left = 0 
        right = len(str(x)) - 1

        while left < right:
            number_left = str(x)[left]
            number_right = str(x)[right]

            if number_left != number_right:
                return False

            else:
                left +=1
                right -=1
        return True
                
