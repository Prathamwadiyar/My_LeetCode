bool predictTheWinner(int* nums, int numsSize) {
    int dp[numsSize];
    
    for (int i = 0; i < numsSize; i++) {
        dp[i] = nums[i];
    }
    
    for (int i = numsSize - 2; i >= 0; i--) {
        for (int j = i + 1; j < numsSize; j++) {
            int pick_left = nums[i] - dp[j];
            int pick_right = nums[j] - dp[j - 1];
            dp[j] = pick_left > pick_right ? pick_left : pick_right;
        }
    }
    
    return dp[numsSize - 1] >= 0;
}