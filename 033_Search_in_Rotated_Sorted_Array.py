class Solution(object):

    def findRotate(self, nums, s, e):
        if nums[e]>nums[s]:
            return -1
        if e-s==1:
            return s
        n = (e+s)/2
        l = self.findRotate(nums, s, n)
        r = self.findRotate(nums, n, e)
        return max(l,r)
        
    def find(self, nums, target, s, e):
        n = (e-s)/2
        if n<0:
            return -1
        if nums[s+n]==target:
            return s+n
        if nums[s+n]>target:
            return self.find(nums, target, s, s+n-1)
        else:
            return self.find(nums, target, s+n+1, e)
                
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        s = 0
        e = len(nums)-1
        if e<0:
            return -1
        elif e==0:
            nums2 = nums
            idx = 0
        else:
            idx = self.findRotate(nums, s, e)
            nums2 = nums[idx+1:]
            nums2.extend(nums[0:idx+1])
        rtn = self.find(nums2, target, s, e)
        if rtn<0: return rtn
        else: return (rtn+1+idx)%len(nums)
