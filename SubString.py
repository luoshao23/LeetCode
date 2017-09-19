# Longest Substring Without Repeating Characters
# Straightforward method


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        best_all = ''
        for i in range(len(s)):
            best = ''
            for sub in s[i:]:
                if sub not in best:
                    best += sub
                else:
                    break
            if len(best) > len(best_all):
                best_all = best
        return len(best_all)

# Rolling window 2n


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        j = 0
        ans = 0
        sets = set()
        while i <= n - ans and j < n:
            if s[j] not in sets:
                sets.add(s[j])
                j += 1
                ans = max(j - i, ans)
            else:
                sets.remove(s[i])
                i += 1
        return ans


# Rolling window n
class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        ans = 0
        sets = {}
        for j in range(n):
            if s[j] in sets:
                i = max(sets[s[j]] + 1, i)
            ans = max(ans, j - i + 1)
            sets[s[j]] = j

        return ans
