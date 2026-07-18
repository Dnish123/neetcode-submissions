class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hshmp= {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]

            if complement in hshmp:
                return[hshmp[complement],i]

            hshmp[nums[i]] = i   