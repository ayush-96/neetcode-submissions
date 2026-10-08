class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if not stack:
                    return False
                ele = stack.pop()
                if (c == ']' and ele != '[') or \
                   (c == '}' and ele != '{') or \
                   (c == ')' and ele != '('):
                    return False
                    
        return len(stack) == 0