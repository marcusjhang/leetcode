class Solution:
    def longestPalindromeSub(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        def expandAroundCenter(left, right):
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]

        max_str = s[0]

        for i in range(len(s)-1):
            even = expandAroundCenter(i,i+1)
            odd = expandAroundCenter(i,i)

            if len(even) > len(max_str):
                max_str = even
            
            if len(odd) > len(max_str):
                max_str = odd

        return max_str 