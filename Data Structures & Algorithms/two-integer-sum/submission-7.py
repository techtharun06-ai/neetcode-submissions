class Solution:
    def twoSum(self, nums, target):
        ha={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in ha:
                return [ha[diff],i]
            ha[n]=i