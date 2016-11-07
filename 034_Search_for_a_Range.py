class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i<len(nums):
            if nums[i]==target: 
                j = i
                while j<len(nums) and nums[j]==target: j+=1
                return [i,j-1]
            elif nums[i]>target: return [-1,-1]
            else: i+=1
        return [-1,-1]
