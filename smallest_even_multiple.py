class Solution(object):
    def smallestEvenMultiple(self, n):
        x = 150 ** 2
        for i in range(1, x + 1):
            if i % 2 == 0 and i % n == 0:
                return i
        


        
