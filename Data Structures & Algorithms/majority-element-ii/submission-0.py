class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        ans = []
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        print(counts)
        for num, count in counts.items():
            if count > len(nums)//3:
                ans.append(num)
        return ans