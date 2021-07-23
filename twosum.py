class Solution:
    def twoSum(self,nums,target):
        dic = {}
        for i,n in enumerate(nums):
            if n in dic:
                return [dic[n], i]
            else:
                dic[target - n] = i 
