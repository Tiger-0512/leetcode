func maxSubArray(nums []int) int {
	max_current := nums[0]
	max_global := max_current

	for _, n := range nums[1:] {
		max_current = maxInt(max_current+n, n)
		max_global = maxInt(max_global, max_current)
	}

	return max_global
}

func maxInt(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}