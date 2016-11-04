class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if (m+n)%2 == 0:
            return float(self.findKth(nums1, nums2, m, n, (m+n)/2) + self.findKth(nums1, nums2, m, n, (m+n)/2+1))/2
        else: 
            return self.findKth(nums1, nums2, m, n, (m+n)/2+1)
        
    def findKth(self, nums1, nums2, m, n, k):
        if m<=0: return nums2[k-1]
        if n<=0: return nums1[k-1]
        if k<=1: return min(nums1[0],nums2[0])
        if nums1[m/2] >= nums2[n/2]:
            if m/2+n/2+1>=k: return self.findKth(nums1[:m/2], nums2, m/2, n, k)
            else:            return self.findKth(nums1, nums2[n/2+1:], m, n-(n/2+1), k-(n/2+1))
        else:
            if n/2+m/2+1>=k: return self.findKth(nums1, nums2[:n/2], m, n/2, k)
            else:            return self.findKth(nums1[m/2+1:], nums2, m-(m/2+1), n, k-(m/2+1))
            
