class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in nums:
            if 0 not in nums:
                return 0
            elif i+1 in nums:
                continue
            else:
                return i+1
        