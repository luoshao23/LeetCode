class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        if l1 > l2:
            nums1, nums2, l1, l2 = nums2, nums1, l2, l1

        i0, j0 = 0, 0
        it, jt = l1 - 1, l2 - 1

        if l1 < 1:
            if l2 < 1:
                return None
            else:
                return float(nums2[l2 // 2] + nums2[(l2 - 1) // 2]) / 2

        for _ in range((l1 + l2 + 1) // 2):
            if i0 >= l1:
                a = nums2[j0]
                j0 += 1
            if j0 >= l2:
                a = nums1[i0]
                i0 += 1
            if i0 < l1 and j0 < l2:
                if nums1[i0] <= nums2[j0]:
                    a = nums1[i0]
                    i0 += 1
                elif nums1[i0] > nums2[j0]:
                    a = nums2[j0]
                    j0 += 1
            if it < 0:
                b = nums2[jt]
                jt -= 1
            if jt < 0:
                b = nums1[it]
                it -= 1
            if it >= 0 and jt >= 0:
                if nums1[it] >= nums2[jt]:
                    b = nums1[it]
                    it -= 1
                elif nums1[it] < nums2[jt]:
                    b = nums2[jt]
                    jt -= 1

        return float(a + b) / 2
