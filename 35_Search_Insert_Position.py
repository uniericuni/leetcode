class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.append(float('Inf'))
        length = len(nums)
        low = 0
        top = length-1
        
        while top is not low:
            n = (top-low)/2
            if target < nums[low+n]:
                top = low+n
            elif target > nums[low+n+1]:
                low = low+n+1
            elif target is nums[low+n]:
                return low+n
            else:
                return low+n+1
        
        return low
