class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            j, k = i + 1, len(nums)-1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] == target and ([nums[i], nums[j], nums[k]] not in ans):
                    ans.append([nums[i], nums[j], nums[k]])
                if nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        return ans