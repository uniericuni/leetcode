class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rtn=-float('inf')
        sum=0
        for num in nums:
            sum=max(num,sum+num)
            rtn=max(rtn,sum)
        return rtn
