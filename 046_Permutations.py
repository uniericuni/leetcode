class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==1:
            return [nums]
        else:
            rtn = []
            for n in nums:
                l = nums[:]
                l.remove(n)
                for rtnl in self.permute(l):
                    tmp = [n]
                    tmp.extend(rtnl)
                    rtn.append(tmp)
            return rtn
