class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i] == 0:
                i+=1
            elif nums[j] == 1 or nums[j] == 2:
                j-=1
            else:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
        
        j = len(nums)-1        
        while i<j:
            if nums[i] == 1:
                i+=1
            elif nums[j] == 2:
                j-=1
            else:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
