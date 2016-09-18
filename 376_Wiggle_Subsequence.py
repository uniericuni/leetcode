class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        ans = 0
        last = 1
        count = 1
        flag = 0
        prev = nums[0]
            
        for n in nums:
            if prev > n and flag >= 0:
                flag = -1
                count += 1
            elif prev < n and flag <= 0:
                flag = 1
                count += 1
            ans = max(count, ans)
            prev = n
            
        return ans
