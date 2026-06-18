class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ll = [0]*len(s)
        for i in range(len(s)):
            ll[i] = s[i]
        yy = [0]*len(t)
        for i in range(len(t)):
            yy[i] = t[i]
        ll = sorted(ll)
        yy = sorted(yy)
        if ll == yy:
            return True
        return False
            
        