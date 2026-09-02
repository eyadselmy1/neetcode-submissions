class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i, num in enumerate(nums):
            h[num] = i

        for i, num in enumerate(nums):
            if num in h and i != h[num]:
                return True
        return False