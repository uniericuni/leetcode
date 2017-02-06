class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        prev1=float('inf');
        prev2=-float('inf');
        i=0; j=0; N=len(nums); rtn=0
        
        while i<N and j<N:
            n=nums[j]
            if n==prev1 and n==prev2:
                j=j+1
            else:
                nums[i]=nums[j]
                prev1=prev2
                prev2=nums[i]
                i=i+1
                j=j+1
                rtn=rtn+1
        
        return rtn
