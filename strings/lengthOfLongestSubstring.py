class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}
        maxLength = 0
        left = 0

        for right in range(len(s)):
            if s[right] not in charDict or charDict[s[right]] < left:
                charDict[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = charDict[s[right]] + 1
                charDict[s[right]] = right

        return maxLength