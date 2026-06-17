class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k=set(nums)
        if len(nums)>len(k):
            return True
        else:
            return False