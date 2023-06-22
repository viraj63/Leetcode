class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict={}  #first create an empty dictionary
        for i in range(len(nums)): # then count the number of elemnt for iteration
            diff=target-nums[i]  #as we know the target we would compare it in dict
            if diff in my_dict: # its there in my_dict then we would return the output
                return [my_dict[diff],i]
            else:
                my_dict[nums[i]]=i   # else we would keep adding in the list
