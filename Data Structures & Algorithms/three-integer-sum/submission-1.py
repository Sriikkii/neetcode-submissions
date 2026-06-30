class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        N = len(nums)
        target = 0

        nums.sort()

        l = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            anchor = nums[i]
            reqTarget = target - anchor
            left = i+1
            right = N-1

            while left < right:
                inside_sum = nums[left]+nums[right]
                if inside_sum < reqTarget:
                    left += 1
                elif inside_sum > reqTarget:
                    right -= 1
                else:
                    l.append([anchor,nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return l
