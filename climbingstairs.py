class Solution:
    def climbstairs(self,n:int):
        a,b = 1,1
        for i in range(n):
            a,b = b, a+b
        return a

