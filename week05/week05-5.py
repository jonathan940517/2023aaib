class Solution(object):
    def mergeAlternately(self, word1, word2):
        w1 = len(word1)
        w2 = len(word2)
        mw = max(w1,w2)
        ans = ''
        for i in range(mw):
            if w1 > i :
                ans += word1[i]
            if w2 > i :
                ans += word2[i]
        return ans
        