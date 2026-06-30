class Solution:
    def isPalindrome(self, s: str) -> bool:





        n = len(s)
        left = 0
        right = n-1



        while left< right:

            while left<right and s[left] not in "qwertyuioplkjhgfdsazxcvbnmMNBVCXZASDFGHJKLPOIUYTREWQ0129384756":
                left += 1
            while left<right and s[right] not in "qwertyuioplkjhgfdsazxcvbnmMNBVCXZASDFGHJKLPOIUYTREWQ0129384756":
                right -= 1

            if left < right:
                str_left = s[left]
                str_right = s[right]

                if 'A' <= str_left <= 'Z':
                    str_left = chr(ord(str_left)+32)
                if 'A' <= str_right <= 'Z':
                    str_right = chr(ord(str_right)+32)

                if str_left != str_right:
                    return False
            
            left += 1
            right -= 1
            
        return True
            
        