class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        seq_sum = nums[0]
        
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                seq_sum += nums[i]
            else:
                break
                
        num_set = set(nums)
        while seq_sum in num_set:
            seq_sum += 1
            
        return seq_sum