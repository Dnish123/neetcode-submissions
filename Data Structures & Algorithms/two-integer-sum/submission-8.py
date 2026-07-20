class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       dic = {}
       n = len(nums)

       for i in range(n):
            complement = target - nums[i]

            if complement in dic:
                return[dic[complement],i]
            dic[nums[i]]= i