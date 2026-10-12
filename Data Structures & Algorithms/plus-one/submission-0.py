class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum=0
        
        for i in range(len(digits)):
            sum=(sum*10)+digits[i]
            res=sum+1
        return [int(x) for x in str(res)]

           