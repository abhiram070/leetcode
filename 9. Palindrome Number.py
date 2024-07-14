class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        n = len(x)
        if n % 2 == 0:
            right = n // 2
            left = right - 1
            while left >= 0 and right < n:
                if x[left] != x[right]:
                    return False
                right += 1
                left -= 1
            return  True
        else:
            right = (n//2) + 1
            left = (n//2) - 1
            while left >= 0 and right < n:
                if x[left] != x[right]:
                    return False
                right += 1
                left -= 1
            return  True
        
        