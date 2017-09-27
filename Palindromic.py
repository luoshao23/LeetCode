def isPal(s):
    l = len(s)
    if l <= 1:
        return True
    half = l // 2 - 1
    for i in range(half, -1, -1):
        if s[i] != s[l - 1 - i]:
            return False
    else:
        return True


class Solution(object):

    def longestPalindrome_1(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l <= 1:
            return s

        for i in range(l, 0, -1):
            for m in range(l - i + 1):
                tmp_s = s[m: m + i]
                print tmp_s
                if isPal(tmp_s):
                    return tmp_s

    def longestPalindrome_2(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l <= 1:
            return s
        longest = ''
        tmp_len = 1

        cstart = 0
        while tmp_len <= l:

            cend = cstart + tmp_len  # excluded
            tmp_str = s[cstart:cend]

            ks = cstart
            ke = cend

            while isPal(tmp_str):

                if len(tmp_str) > len(longest):
                    longest = tmp_str
                    tmp_len = len(longest)

                if ks - 1 < 0 or ke + 1 > l:
                    tmp_len += 1
                    cstart = 0
                    break

                ks -= 1
                ke += 1
                tmp_str = s[ks:ke]
            else:
                if cstart + tmp_len >= l:
                    tmp_len += 1
                    cstart = 0
                else:
                    cstart += 1

        return longest

class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        slen = len(s)
        if slen <= 1:
            return s

        longest_str = ''
        cp = 0

        while cp < slen:
            left = cp - 1
            right = cp + 1
            tmp_str = s[cp]
            while left >= 0 and right < slen and s[left] == s[right]:
                tmp_str = s[left] + tmp_str + s[right]
                left -= 1
                right += 1

            if len(tmp_str) > len(longest_str):
                longest_str = tmp_str

            left = cp
            right = cp + 1
            tmp_str = ''
            while left >= 0 and right < slen and s[left] == s[right]:
                tmp_str = s[left] + tmp_str + s[right]
                left -= 1
                right += 1

            if len(tmp_str) > len(longest_str):
                longest_str = tmp_str

            cp += 1
        return longest_str

    def expandAroundCenter(s, left, right):
        L, R = left, right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1

    def longestPalindrome_2(self, s):
        st, end = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i+1)
            lens = max(len1, len2)
            if lens > end-st:
                st = i-(lens-1)//2
                end = i + lens//2

        return s[st:end+1]

## Manacher algorithm
def preprocess(s):
    if len(s) == 0:
        return '^$'
    snew = '^#'
    for si in s:
        snew += si + '#'
    snew += '$'
    return snew
class Solution(object):
    def longestPalindrome(self, s):
        T = preprocess(s)
        n = len(T)
        p = [None for i in range(n)]
        C, R = 0, 0
        for i in range(1, n - 1):
            i_mirror = 2 * C - i
            p[i] = min(R - i, p[i_mirror]) if R > i else 0

            while T[i+1+p[i]]==T[i-1-p[i]]:
                p[i] += 1

            if i+p[i] > R:
                C = i
                R = i + p[i]

        maxLen = 0
        centerIndex = 0
        for i in range(1, n-1):
            if p[i] > maxLen:
                maxLen = p[i]
                centerIndex = i

        return s[(centerIndex-1-maxLen)//2:(centerIndex-1-maxLen)//2+maxLen]