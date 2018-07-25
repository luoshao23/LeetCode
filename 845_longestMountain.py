class Solution:
    def longestMountain(self, A):
        n = len(A)
        up, down = [0] * n, [0] * n
        for i in range(1, n):
            if A[i] > A[i - 1]:
                up[i] = up[i - 1] + 1
        for i in range(n - 1)[::-1]:
            if A[i] > A[i + 1]:
                down[i] = down[i + 1] + 1
        return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])

    # Advance: one pass and O(1)
    def longestMountain2(self, A):
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]:
                up = down = 0
            up += A[i - 1] < A[i]
            down += A[i - 1] > A[i]
            if up and down:
                res = max(res, up + down + 1)
        return res
