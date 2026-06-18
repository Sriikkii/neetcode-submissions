class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}
        ll = [[] for i in range(len(nums)+1)]
        val = 0
        for idx ,value in enumerate(nums,start=1):
            if value not in hashmap:
                hashmap[value] = 1
            else:
                hashmap[value] += 1
        
        for number , count in hashmap.items():
            ll[count].append(number)

        l = []

        ll.reverse()

        for i in ll:
            for j in i :
                l.append(j)
                if len(l) == k:
                    return l
                
        
"""        for i in range(len(ll)-1,0,-1):
            for j in ll[i]:
                l.append(j)
                if len(l) == k:
                    return l"""
         