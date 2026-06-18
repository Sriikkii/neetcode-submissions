from collections import defaultdict 
import string 
import math
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        st = list(string.ascii_lowercase)
        hm = {}
        for idx,letter in enumerate(st):
            hm[letter] = l[idx]

        ll = []
        
        val = 1
        for i in range(len(strs)):
            val = 1
            for j in strs[i]:
                val *= hm[j]
            ll.append(val)
        print(ll)
        hashmap = {}
        for i in range(len(ll)):
            if ll[i] not in hashmap:
                hashmap[ll[i]] = [strs[i]]
            else:
                hashmap[ll[i]].append(strs[i])
        return list(hashmap.values())


                




            

         




            


        

        

        