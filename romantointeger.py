class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        while i+1 <len(s):
            if d[s[i]] >= d[s[i+1]]:
                sum = sum + d[s[i]]
            else:
                sum = sum + (d[s[i+1]] - d[s[i]])
                i+=1
            i+=1
        if i < len(s):
            sum = sum + d[s[i]]
        return sum