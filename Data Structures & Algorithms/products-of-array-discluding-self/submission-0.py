class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        # prefix product 

        #[1,1,1,1]
        prefix = 1 
        for i in range(len(nums)): 
            res[i] = prefix 
            prefix *= nums[i]

        # sufix product 
        sufix = 1 
        for i in range(len(nums)-1, -1, -1): 
            res[i] *= sufix 
            sufix *= nums[i]
        return res 