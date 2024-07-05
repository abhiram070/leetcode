class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        string = [""] * numRows
        j = 0

        while j < len(s):
            for i in range(numRows):
                if j < len(s):
                    string[i] += s[j]
                    j += 1
            for i in range(numRows-2, 0, -1):
                if j < len(s):
                    string[i] += s[j]
                    j += 1
        return "".join(string)  
      