class Solution(object):
    def longestPalindrome(self, s):
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Odd-length palindromes
            substr1 = expand_around_center(i, i)
            if len(substr1) > len(longest):
                longest = substr1
            
            # Even-length palindromes 
            substr2 = expand_around_center(i, i + 1)
            if len(substr2) > len(longest):
                longest = substr2
        
        return longest
  
