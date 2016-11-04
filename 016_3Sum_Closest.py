class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        self.rtn = float('inf')
        nums.sort()
        prev = float('inf')
        for i,num in enumerate(nums):
            if num == prev: continue
            self.twoSum(nums[i+1:], target, target-num)
            prev = num
        return self.rtn

    def twoSum(self, nums, target, sum):
        l = 0
        r = len(nums)-1
        while(l<r):
            diff = sum - nums[l] - nums[r]
            if abs(diff) < abs(target-self.rtn): self.rtn = target-diff
            if diff > 0: l+=1
            elif diff < 0: r-=1
            else: return target
                
