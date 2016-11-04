class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        it = range(0,len(nums))
        it.reverse()
        i = 0
        for i in it:
            if i-1<0: break
            if nums[i]>nums[i-1]: break
        if i-1<0:
            nums.reverse()
        else:
            for j in it:
                if nums[j]>nums[i-1]: break
            temp = nums[j]
            nums[j] = nums[i-1]
            nums[i-1] = temp
            s = nums[i:]
            s.sort()
            nums[i:] = s
