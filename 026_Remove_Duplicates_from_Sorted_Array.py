class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numTable = {}
        count = 0
        m = len(nums)
        prev = None
            
        for n in range(0,m):
            if nums[0] is None or nums[0] > prev:
                nums.append(nums[0])
                prev = nums[0]
                count += 1
            nums.pop(0)
                
        return count
