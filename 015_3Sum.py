class Solution(object):
    
    def twoSum(self, nums, sum, rtn):
        dict = {}
        for num in nums:
            if sum-num in dict:
                if dict[sum-num]:
                    dict[sum-num] = False
                    rtn.append([-sum, sum-num, num])
            if num not in dict:
                dict[num] = True
            
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    
        nums.sort()
        rtn = []
        prev = float('inf')
        for i,num in enumerate(nums):
            if num == prev:
                continue
            self.twoSum(nums[i+1:], -num, rtn)
            prev = num
        return rtn
