#Brute force
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j :
                    continue
                l[i] *= nums[j]
        return l

        