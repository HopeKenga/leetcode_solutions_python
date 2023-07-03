class Solution(object):
    def removeDuplicates(self, nums):
        #O(n) time and O(1)space
        #since we need to solve this in-place, we will use pointers
        #have two pointers
        #whenever two values are not the same, replace pointer values
        # 0, 0,  1,  1,  1,  2,  2,  3,  3,  4 - input
             #l
             #r
                #r-1
        # 0, 1, 2, 3, 4  
        #return 5 which is the position of left pointer/ 1st five elements
        
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left

        