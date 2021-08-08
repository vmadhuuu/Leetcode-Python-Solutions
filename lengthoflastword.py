class Solution:
    def lengthoflastWord(self, s):
        return 0 if not s.split else len(s.split)[-1]