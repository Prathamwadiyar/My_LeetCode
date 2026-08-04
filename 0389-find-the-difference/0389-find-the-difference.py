class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for char in s + t:
            ans ^= ord(char)
        return chr(ans)