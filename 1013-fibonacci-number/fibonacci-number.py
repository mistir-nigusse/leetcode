class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        prev1, prev2 = 1, 0  # Initialize F(1) and F(0)
        
        for i in range(2, n + 1):
            current = prev1 + prev2  # F(n) = F(n-1) + F(n-2)
            prev2 = prev1  # Move prev2 to prev1
            prev1 = current  # Move current to prev1
        
        return prev1  # This will hold F(n)
