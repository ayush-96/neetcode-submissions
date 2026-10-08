from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for operation in operations:
            if operation == 'C':
                stack.pop()
            elif operation == 'D':
                stack.append(stack[-1]*2)
            elif operation == '+':
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(operation))
        ans = sum(ele for ele in stack)
        return ans