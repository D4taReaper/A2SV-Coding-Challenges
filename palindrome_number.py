class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        reverse = x[ : : - 1]
        if reverse == x:
            return True
        return False
        
        
