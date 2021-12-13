class Solution:
    def palindrome(self, x:int) -> bool:
        return False if x<=0 else x==int(str(x)[::-1])
