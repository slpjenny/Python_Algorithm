class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        #start = 0
        #end = len(nums)-1

        if target in nums:
            return nums.index(target)

        else:
            nums.append(target)
            return sorted(nums).index(target)
