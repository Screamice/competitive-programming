class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype prefix: str
        """
        if not strs: return ""

        s1, s2 = max(strs), min(strs)
        i, match = 0, 0
        while i<len(s1) and i<len(s2) and s1[i] == s2[i]:
            i, match = i+1, match+1
        return s1[0:match]
sol = Solution()
print(sol.longestCommonPrefix(["flower","flows","flight"]))