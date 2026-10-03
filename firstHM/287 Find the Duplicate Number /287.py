class Solution(object):
    def findDuplicate(self, nums):
        low, hi = 1, len(nums) - 1
        while low < hi:
            mid = (low + hi) // 2
            count = 0
            for x in nums:
                if x <= mid:
                    count += 1
            if (count > mid):
                hi = mid
            else:
                low = mid + 1
        return low
