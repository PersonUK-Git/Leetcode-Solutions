class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in charset:
                print(s[l])
                charset.remove(s[l])
                l += 1
                print(l)
            charset.add(s[i])
            res = max(res, i - l + 1)
        return res

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))