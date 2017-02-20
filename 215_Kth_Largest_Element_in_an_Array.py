class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        rtn=sorted(nums)
        rtn=rtn[::-1]
        return rtn[k-1]
