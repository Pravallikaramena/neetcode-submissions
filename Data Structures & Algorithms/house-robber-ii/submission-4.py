class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
           return 0
        if n==1:
            return nums[0]
        def pais(houses):
            first,second=0,0
            for i in houses:
               first,second=second,max(second,first+i)
            return second
        case1=pais(nums[:-1])
        case2=pais(nums[1:])
        return max(case1,case2)


        