class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros = nums.count(0)
        ones = nums.count(1)
        twos = nums.count(2)
        
        nums[:zeros] = [0] * zeros
        nums[zeros:zeros+ones] = [1] * ones
        nums[zeros+ones:] = [2] * twos