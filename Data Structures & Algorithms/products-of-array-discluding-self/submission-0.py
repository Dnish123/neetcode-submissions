class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
    # Create array of size n + 1 filled with zeros
        pref = [0] * (n)
    
        for i in range(n):
            prod = 1
            for j in range(n):
                if i ==j:
                    continue
                prod *=nums[j]
            
            pref[i] = prod
        
        return pref


        


        