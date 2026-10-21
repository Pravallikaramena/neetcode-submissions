class Solution:
    def expansion(self,s,left,right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==0:
            return " "
        longest=s[0]
        for i in range(n):
            odd_p=self.expansion(s,i,i)
            even_p=self.expansion(s,i,i+1)
            if len(odd_p) >len(longest):
                longest=odd_p
            if len(even_p) > len(longest):
                longest=even_p
        return longest

        