class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        n1,n2=1,0
        for i in range(n-1,-1,-1):
            c=0
            if(s[i]!="0"):
               c=n1
               if i+1<n and 10<=int(s[i:i+2])<=26:
                   c+=n2
            n1,n2=c,n1
        return n1
            


              

        