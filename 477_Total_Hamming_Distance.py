class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rtn = 0
        n = len(nums)
        for m in range(0,32):
            count = 0
            for i in range(0,n):
                if bin(nums[i])[-1]=='1':
                    count += 1
                nums[i] = nums[i]>>1
            rtn += count*(n-count)
        return rtn
