class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counters = {}
        for num in nums:
            counters[num] = counters.get(num, 0) + 1
        sorted_counters = sorted(counters, key=lambda x: counters[x], reverse=True)
        print(sorted_counters)
        return sorted_counters[0]