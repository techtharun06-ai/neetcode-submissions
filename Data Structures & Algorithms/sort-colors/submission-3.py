class Solution:
    def sortColors(self, nums: List[int]) -> None:
        z=nums.count(0)
        o=nums.count(1)
        t=nums.count(2)
        nums[:z]=[0]*z
        nums[z:z+o]=[1]*o
        nums[z+o:]=[2]*t