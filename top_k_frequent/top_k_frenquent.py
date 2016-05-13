from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = Counter()
        for i in nums:
            cnt[i] += 1
        r = cnt.most_common(k)
        return [ x for x,y in r ]
        
