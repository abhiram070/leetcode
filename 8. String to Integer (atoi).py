class Solution(object):
    def myAtoi(self, s):
        newS = ''
        sign = ''
        for char in s:
            if char == ' ' and not sign and not newS:
                continue
            if not sign and char in '-+' and not newS:
                sign = char
                continue
            if char.isdigit():
                newS += char
            else:
                break
        
        if not newS or (newS == '-' or newS == '+'):
            return 0

        if sign == '-':
            newS = '-' + newS.lstrip('0') or '-0' 

        try:
            newS = int(newS)
        except ValueError:
            return 0
        if newS < -2147483648:
            newS = -2147483648 
        if newS > 2147483647:
            newS = 2147483647
        
        return newS