class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        counts = Counter(nums)
        sort_count = sorted(counts, key=lambda x: counts[x], reverse=True)
        print(sort_count[:k])
        return sort_count[:k]