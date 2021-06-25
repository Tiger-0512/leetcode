func rob(nums []int) int {
	dp := make([]int, len(nums)+1)
	dp[1] = nums[0]

	for i := 2; i < len(dp); i++ {
		dp[i] = maxInt(dp[i-1], dp[i-2]+nums[i-1])
	}
	return dp[len(dp)-1]
}

func maxInt(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}