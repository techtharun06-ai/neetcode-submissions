class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        pr=1
        for i in range(n):
            res[i]*=pr
            pr*=nums[i]
        po=1
        for j in range(n-1,-1,-1):
            res[j]*=po
            po*=nums[j]
        return res
        
        