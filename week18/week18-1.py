class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        dic = ['a','e','i','o','u','A','E','I','O','U']
        temp = len(s) // 2
        ansa = 0
        ansb = 0
        for i in range(len(s)):
            if i < temp:
                if s[i] in dic:
                    ansa += 1
            else:
                if s[i] in dic:
                    ansb+= 1
        if ansa == ansb:
            return True
        else:
            return False