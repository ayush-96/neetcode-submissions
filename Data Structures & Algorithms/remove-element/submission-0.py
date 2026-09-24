class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occ = nums.count(val)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = float('inf')
        nums.sort()
        return len(nums)-occ