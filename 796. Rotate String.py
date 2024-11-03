class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s+s


sol = Solution()

print(sol.rotateString("abcde", "cdeab"))