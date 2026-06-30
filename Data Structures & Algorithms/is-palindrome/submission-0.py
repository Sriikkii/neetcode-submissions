class Solution:
    def isPalindrome(self, s: str) -> bool:



        strs = ""
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90:
                strs += chr(ord(s[i])+32)
            elif 48<= ord(s[i])<=57:
                strs += s[i]
            elif 97<=ord(s[i])<=122:
                strs += s[i]
            continue

        n = len(strs)
        left = 0
        right = n-1



        while left< right:

            if strs[left] != strs[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
            
        