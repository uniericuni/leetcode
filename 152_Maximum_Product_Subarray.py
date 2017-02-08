class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:return 0
        pM=nums[0]
        pm=nums[0]
        rtn=nums[0]
        for num in nums[1:]:
            temp=pM
            pM=max(max(pM*num,pm*num),num)
            pm=min(min(temp*num,pm*num),num)
            rtn=max(rtn,pM)
        return rtn
