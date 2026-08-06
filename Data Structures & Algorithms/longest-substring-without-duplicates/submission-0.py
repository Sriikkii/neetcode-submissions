class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        n = len(s)
        left = 0
        right = 0
        longest_length = 0
        for right in range(n):
            while(s[right] in sett):
                sett.remove(s[left])
                left += 1
            window_length = (right-left)+1
            longest_length = max(window_length,longest_length)
            sett.add(s[right])
        return longest_length



        