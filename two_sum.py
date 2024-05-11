class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(j != i):
                    if (nums[i] + nums[j] == target):
                        return i,j
nums = [2,7,11,15]
target = 9
solution = Solution()    
value1,value2 = solution.twoSum(nums,target) 