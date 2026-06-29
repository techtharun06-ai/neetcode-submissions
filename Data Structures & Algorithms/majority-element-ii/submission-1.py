class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=None
        c2=None
        count1=0
        count2=0
        for i in nums:
            if i==c1:
                count1+=1
            elif i==c2:
                count2+=1
            elif count1==0:
                c1=i
                count1=1
            elif count2==0:
                c2=i
                count2=1
            else:
                count1-=1
                count2-=1
        res=[]
        if nums.count(c1)>len(nums)//3:
            res.append(c1)
        if c2!=c1 and nums.count(c2)>len(nums)//3:
            res.append(c2)
        return res    

