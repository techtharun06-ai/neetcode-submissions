class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        l=len(nums)-1
        oc=0
        while i<=l:
            if nums[i]==val:
                nums[i],nums[l]=nums[l],nums[i]
                oc+=1
                l-=1
            else:
                i+=1
        return i

        