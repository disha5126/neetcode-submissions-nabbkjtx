class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(i for i in s if i.isalnum())
        s=s.lower()
        if s==s[::-1]:
            return True
        else:
            return False
        