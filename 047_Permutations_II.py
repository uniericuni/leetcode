class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums)==1:
            return [nums]
        else:
            rtn = []
            for n in list(set(nums)):
                l = nums[:]
                l.remove(n)
                for rtnl in self.permuteUnique(l):
                    temp = [n]
                    temp.extend(rtnl)
                    rtn.append(temp)
            return rtn
