class Solution:
    def twoSum(self, nums, target):
        h={}
        for i,n in enumerate(nums):
            d=target-n
            if d in h:
                return [h[d],i]
            h[n]=i
    
