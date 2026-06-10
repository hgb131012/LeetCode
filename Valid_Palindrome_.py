class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join([c.lower() for c in s if c.isalnum()])
        return string[::-1] == string
