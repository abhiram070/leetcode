class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d = ""
        for i in range (1,len(s)):
            count = 0
            for j in range (len(d)):
                if s[i] == d[j]:
                    count = 1
                    break
            if count == 0:
                d = d + s[i]           
        return len(d)

sol = Solution()
s = "abcabcbb"
result = sol.lengthOfLongestSubstring(s)
print("The answer is ",result)      