from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        co=Counter(nums)
        return [num for num,freq in co.most_common(k)]