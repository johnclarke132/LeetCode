class Solution:
    def isPalindrome(self, x: int) -> bool:
        if float(x) < 0:
            return False
        if str(x) == str(x)[::-1]:
            return True
        return False
