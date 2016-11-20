class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dict = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in dict: dict[key].append(str)
            else: dict[key] = [str]
        
        return [dict[key] for key in dict]
