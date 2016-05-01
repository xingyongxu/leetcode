def findMedianOfSingleSortedArray(l):
    ''' Array l must not be []'''
    length = len(l)
    if length % 2 == 0:
        return (l[length/2] + l[length /2 - 1])/2.
    return l[length/2]

# there're only 2 numbers in nums1, and nums2 has even elements(n>0)
def least_2_even(nums1, nums2):
    a, b = nums1[0],nums1[1]
    len2 = len(nums2)
    p, q = nums2[len2 / 2 - 1], nums2[len2 / 2]
    if b <= q and p <= a:
        return (a + b) / 2.
    if b <= p:
        if len2 > 2:
            return (max(b, nums2[len2 / 2 - 2]) + p) / 2.
        return (b + p) / 2.
    if a >= q:
        if len2 > 2:
            return (min(a, nums2[len2 / 2 + 1]) + q) / 2.
        return (a + q) / 2.
    if a <=p and q <=b:
        return (p + q) / 2.
    if p <= a <= q <= b:
        return (a + q) / 2.
    return (b + p) / 2.

def least_2_odd(nums1, nums2):
    a, b = nums1[0],nums1[1]
    len2 = len(nums2)
    m = nums2[len2 / 2]
    if a <= m <= b:
        return m
    if b <= m:
        if len2 > 1:
            return max(b, nums2[len2 / 2 - 1])
        return b
    if m <= a:
        if len2 > 1:
            return min(a, nums2[len2 / 2 + 1])
        return a

def least_1_odd(nums1, nums2):
    a = nums1[0]
    len2 = len(nums2)
    m = nums2[len2 / 2]
    if len2 > 1:
        if a >= nums2[len2 / 2]:
            return (min(a, nums2[len2 / 2 + 1]) + m) / 2.
        else:
            return (max(a, nums2[len2 / 2 - 1]) + m) / 2.
    else:
        return (a + m) / 2.

def least_1_even(nums1, nums2):
    a = nums1[0]
    len2 = len(nums2)
    p, q = nums2[len2 / 2 - 1], nums2[len2 / 2]
    if p <= a <= q:
        return a
    if a < p:
        return p
    return q

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1:
            return findMedianOfSingleSortedArray(nums2)
        if not nums2:
            return findMedianOfSingleSortedArray(nums1)
        len1, len2 = len(nums1),len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)

        if len1 == 1:
            if len2 % 2 == 0:
                return least_1_even(nums1, nums2)
            else:
                return least_1_odd(nums1, nums2)

        if len1 == 2:
            if len2 % 2 == 0:
                return least_2_even(nums1, nums2)
            else:
                return least_2_odd(nums1, nums2)

        if nums1 and nums2:
            m1 = findMedianOfSingleSortedArray(nums1)
            m2 = findMedianOfSingleSortedArray(nums2)
            if m1 == m2:
                return m1
            if m1 < m2:
                if len1 % 2 == 0:
                    return self.findMedianSortedArrays(nums1[len1 / 2 - 1:], nums2[:len2 - len1 / 2 + 1])
                return self.findMedianSortedArrays(nums1[len1 / 2:], nums2[: len2 - len1 / 2])
            else:
                if len1 % 2 == 0:
                    return self.findMedianSortedArrays(nums1[:len1 / 2 + 1 ], nums2[len1 / 2 - 1:])
                return self.findMedianSortedArrays(nums1[:len1 / 2 + 1 ], nums2[len1 / 2:])
