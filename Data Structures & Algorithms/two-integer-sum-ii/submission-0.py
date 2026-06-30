class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        n = len(numbers)
        right = n-1

        while left <= right:

            target_checker = numbers[left]+numbers[right]

            if target_checker < target:
                left += 1
            elif target_checker > target:
                right -= 1
            
            if target_checker == target:
                return [left+1 , right+1]

        