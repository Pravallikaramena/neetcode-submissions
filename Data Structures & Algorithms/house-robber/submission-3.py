class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        first=nums[0]
        second=max(first,nums[1])
        for i in range(2,n):
            current=max(second,first+nums[i])
            first,second=second,current
        return second


            