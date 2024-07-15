class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        char = len(s) - 1
        
        while char >= 0:
            if char > 0 and symbols[s[char]] > symbols[s[char - 1]]:
                result += symbols[s[char]] - symbols[s[char - 1]]
                char -= 2
            else:
                result += symbols[s[char]]
                char -= 1
        
        return result
        