class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diction = {}
        for i in s:
            if i in diction:
                diction[i] = diction[i] + 1
            else:
                diction[i] = 1
        for i in t:
            if i not in diction:
                return i
            if diction[i] ==0:
                return i
            else:
                diction[i] = diction[i]-1