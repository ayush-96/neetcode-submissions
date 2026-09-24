class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counters = {}
        for char in s:
            counters[char] = counters.get(char, 0) + 1
        for char in t:
            if char not in counters or counters[char] == 0:
                return False
            counters[char] -= 1
        return True