class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = "[{("
        valid = ["()", "[]", "{}"]
        for c in s:
            if c in open:
                stack.append(c)
                continue
            if not stack:
                return False
            temp = stack.pop() + c
            if temp not in valid:
                return False
        return len(stack ) == 0