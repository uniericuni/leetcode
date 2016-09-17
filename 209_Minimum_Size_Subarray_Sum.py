class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        j = 0
        ans = len(nums)+1
        sums = 0
        
        while j>=i:
            if sums >= s:
                ans = min(ans, j-i)
                sums -= nums[i]
                i += 1
            else:
                if j>=len(nums):
                    break;
                sums += nums[j]
                j += 1
            
        if ans > len(nums):
            return 0
        else:
            return ans
