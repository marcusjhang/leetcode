class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_dict = {}
        has_odd = False
        res = 0

        for ltr in s:
            char_dict[ltr] = 1 + char_dict.get(ltr, 0)
        
        for count in char_dict.values():
            if count % 2:
                has_odd = True
                count -= 1
            
            res += count

        if has_odd:
            res += 1

        return res