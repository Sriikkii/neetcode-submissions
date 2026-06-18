class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,n in enumerate(nums):
            t = target - n
            if t in hashmap:
                return [hashmap[t],i]
            hashmap[n] = i
        return [] 

        