class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        count = 0

        for i in range(len(nums)):
            left = (i == 0 or nums[i-1] == 0)
            right = (i == len(nums)-1 or nums[i+1] == 0)

            if nums[i] == 0 and left and right:
                nums[i] = 1
                count += 1

        return count >= n