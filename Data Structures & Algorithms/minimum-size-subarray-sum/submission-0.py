class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        res = len(nums)
        l, tmp = 0, 0
        for r in range(len(nums)):
            tmp += nums[r]
            while tmp >= target:
                res = min(res, (r - l+ 1))
                tmp -= nums[l]
                l += 1
        return res