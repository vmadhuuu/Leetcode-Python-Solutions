class Solution:
    def findallNumbers(self, nums: List[int]):
        result = [i for i in range(0, len(nums) + 1)]
        for i in nums: result[i] = 0
        return [i for i in result if i != 0]
