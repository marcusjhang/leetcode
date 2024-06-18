class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. remove white spaces and others
        # 2. check whether it is a palindrome 

        new = ''
        for a in s:
            if a.isalpha() or a.isdigit():
                new += a.lower()
        
        return new == new[::-1]
    
# T O(n) S O(n) 