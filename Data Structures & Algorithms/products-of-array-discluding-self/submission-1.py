class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr = []
        sf = []
        l = []
        n = len(nums)
        for i in range(n):
            pr = nums[:i]
            sf = nums[i+1:]
            mpr = 1
            msf = 1
            for j in pr :
                mpr *= j
            for k in sf:
                msf *= k
            l.append(mpr*msf)
        return l


        