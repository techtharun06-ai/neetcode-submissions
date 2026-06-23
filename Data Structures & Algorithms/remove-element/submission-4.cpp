class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left=0,right=nums.size()-1;
        int occ=0;
        while(left<=right)
        {
            if(nums[left]==val)
            {
                int temp=nums[right];
                nums[right]=nums[left];
                nums[left]=temp;
                right--;
                occ++;
            }
            else
            {
                left++;
            }
        }
        return left;
        
    }
};