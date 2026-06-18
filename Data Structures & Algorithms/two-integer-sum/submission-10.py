class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,v in enumerate(nums):
            hashmap[i] = v
        
        l = list(hashmap.values())
        temp = l.copy()
        for k,v in hashmap.items():
            t = target-v
            
            if t in l:
                g = l.index(t)
                if g!=k:
                    if k>g:
                        return [g,k]
                    else:
                        return[k,g]
        return []
                





        

        