class Solution(object):
    def reverse(self, x):
        s = str(x)

        if s[-1] == '0' and len(s) > 1:
            s = s[:-1]
        if s[0] == '-':
            reversed_integer = int('-' + s[:0:-1])

        else:
            reversed_integer = int(s[::-1])
        
        if reversed_integer < -2**31 or reversed_integer > 2**31 - 1:
            return 0

        return reversed_integer