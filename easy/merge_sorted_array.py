class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0

        for val in nums2:
            while i < m and nums1[i] < val:
                i += 1

            for idx in reversed(range(i, m)):
                nums1[idx + 1] = nums1[idx]
            nums1[i] = val
            m += 1

    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if m > 0 and nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1


if __name__ == '__main__':
    l1 = [0]
    l2 = [1]
    Solution().merge2(l1, 0, l2, len(l2))
    print(l1)
