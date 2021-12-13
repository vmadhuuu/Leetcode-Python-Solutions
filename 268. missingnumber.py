class Solution:
    def MissingNumber(self, nums: List[str]) --> int:
        n = len(nums) + 1
        total = int((n/2) - (n-1))
        return total - sum(nums)
