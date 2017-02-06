class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dict={}
        sum=0
        maxVal=-float('inf')
        dict[0]=-1
        for i,num in enumerate(nums):
            sum=sum+num
            key=sum-k
            if key in dict:
                maxVal=max(maxVal,i-dict[key])
            if sum not in dict:
                dict[sum]=i
            
        if maxVal==-float('inf'):
            return 0
        return maxVal
