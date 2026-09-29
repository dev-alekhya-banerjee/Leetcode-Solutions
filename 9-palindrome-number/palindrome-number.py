class Solution:
    def isPalindrome(self, x: int) -> bool:
        d=x
        rd=0
        while x>0:
            ld=x%10
            x=x//10
            rd=(rd*10)+ld
        if rd==d:
            return True
        else:
            return False