func rob(nums []int) int {
	l := len(nums)
	if l == 0 {
		return 0
	}
	if l == 1 {
		return nums[0]
	}
	return max(helper(nums[:(l-1)]), helper(nums[1:]))
}

func helper(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}
	dp := []int{nums[0], max(nums[0], nums[1])}
	for i := 2; i < len(nums); i++ {
		index := i % 2
		dp[index] = max(dp[index]+nums[i], dp[(index+1)%2])
	}
	return max(dp[0], dp[1])
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
