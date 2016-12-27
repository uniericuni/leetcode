class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        rtn=0
        for num in nums:
            dict[num]=True
            
        for key in dict:
            if dict[key]:
                len=1
                dict[key]=False
                val=key
                while val+1 in dict:
                    len+=1
                    dict[val+1]=False
                    val+=1
                val=key    
                while val-1 in dict:
                    len+=1
                    dict[val-1]=False
                    val-=1
            rtn=max(len,rtn)
        
        return rtn
