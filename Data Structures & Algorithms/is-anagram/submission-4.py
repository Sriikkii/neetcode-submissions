class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = {}
        hashmapT = {}

        if len(s)!= len(t):
            return False

        for i in s :
            if i not in hashmapS:
                hashmapS[i] = 1
            else:
                hashmapS[i] += 1

        for i in t :
            if i not in hashmapT:
                hashmapT[i] = 1
            else:
                hashmapT[i] += 1
        
        for k,v in hashmapS.items():
            if k not in hashmapT:
                return False
            if v != hashmapT[k]:
                return False
        return True            
            
        