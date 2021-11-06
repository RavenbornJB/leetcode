class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greatest = {}
        s = [0]
        for i in range(1, len(nums2)):
            while s and nums2[i] > nums2[s[-1]]:
                next_greatest[nums2[s.pop()]] = nums2[i]
            s.append(i)

        return [next_greatest.get(val, -1) for val in nums1]


if __name__ == '__main__':
    n1 = [4, 1, 2]
    n2 = [1, 3, 4, 2]
    print(Solution().nextGreaterElement(n1, n2))
