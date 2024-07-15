class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbols = ['I','V','X','L','C','D','M']
        result = ''
        i = 0
        while num > 0 and i <= 5:
            digit = num % 10
            num = num // 10
            if digit == 0:
                pass
            elif digit < 4:
                for j in range(digit):
                    result = symbols[i] + result
            elif digit == 4:
                result = symbols[i+1] + result
                result = symbols[i] + result
            elif digit == 5:
                result = symbols[i+1] + result
            elif digit < 9:
                for j in range (digit - 5):
                    result = symbols[i] + result
                result = symbols[i+1] + result
            elif digit == 9:
                result = symbols[i+2] + result
                result = symbols[i] + result
                
            i += 2
        if num > 0:
            for _ in range(num):
                result = symbols[6] + result
        return result