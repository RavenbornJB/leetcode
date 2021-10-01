class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # b/s pivot
        start = 0
        end = len(nums) - 1
        while end - start > 1 and nums[start] > nums[end]:
            mid = (start + end) // 2
            if nums[mid] > nums[start]:
                start = mid + 1
            else:  # mid < end
                end = mid

        pivot = min(start, end, key=lambda x: nums[x])

        # b/s target
        start = pivot
        end = start + len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid % len(nums)]:
                return mid % len(nums)
            elif target < nums[mid % len(nums)]:
                end = mid - 1
            else:
                start = mid + 1

        return -1


if __name__ == '__main__':
    n = [1]
    t = 0
    print(Solution().search(n, t))
