class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = {}
        hashmapT = {}

        if len(s)!= len(t):
            return False

        for i in s :
            hashmapS[i] = hashmapS.get(i, 0) + 1

        for i in t :
            hashmapT[i] = hashmapT.get(i, 0) + 1
        
        for k,v in hashmapS.items():
            if k not in hashmapT:
                return False
            if v != hashmapT[k]:
                return False
        return True            
            
        
