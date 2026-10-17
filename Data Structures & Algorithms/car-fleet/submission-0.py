class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined_pos = [(p, s) for p, s in zip(position, speed)]
        sorted_pos = sorted(combined_pos, key=lambda x: x[0], reverse=True)
        stack = []
        for p,s in sorted_pos:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)