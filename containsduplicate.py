class Solution:
    def duplicate(self, nums: List[int]):
        table = set()
        for i in nums:
            if i in table:
                return True
            else:
                table.add(i)
        return False
