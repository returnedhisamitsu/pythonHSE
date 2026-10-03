class Solution(object):
    def isMonotonic(self, nums):
        i = 0
        while (i < (len(nums) - 1) and nums[i] == nums[i+1]):
            i += 1
        if i == (len(nums) - 1):
            return True
        if (nums[i] > nums[i+1]):
            for j in range(i + 1, len(nums) - 1):
                if nums[j] < nums[j+1]:
                    return False
        else:
            for j in range(i + 1, len(nums) - 1):
                if nums[j] > nums[j+1]:
                    return False
        return True