class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashtable = {};
        re = [];
        flag = 0;
        count = 0;
        
        for num in nums:
            
            if str(num) in hashtable.keys():
                ans = hashtable[str(num)];
                re.append(ans[1]);
                re.append(count);
                flag = 1;
            if flag == 1:
                break;
            com = target - num;
            hashtable[str(com)] = (num, count);
            count += 1;
        
        return re;
