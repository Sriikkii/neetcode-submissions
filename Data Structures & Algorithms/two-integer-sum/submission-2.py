class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ll = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i]+nums[j] == target:
                    if i>j:
                        return [j,i]
                    else:
                        return [i,j]
        

        