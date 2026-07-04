class Solution:
    def validPalindrome(self, s: str) -> bool:
        counter = 0
        left = 0
        n = len(s)
        right =  n-1
        while left <= right:
            if s[left] != s[right]:
                skip_left = True
                skip_right = True
                t1,t2 = left+1 , right
                while t1<=t2:
                    if s[t1]!=s[t2]:
                        skip_left = False
                    t1+=1
                    t2-=1
                t1,t2 = left,right-1
                while t1<=t2:
                    if s[t1]!=s[t2]:
                        skip_right = False
                        break
                    t1 += 1
                    t2 -= 1
                return skip_left or skip_right
            left+=1
            right-=1
        return True
        