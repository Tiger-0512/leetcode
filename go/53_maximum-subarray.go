func maxSubArray(nums []int) int {
	maxCurrent := nums[0]
	maxGlobal := maxCurrent

	for _, n := range nums[1:] {
		maxCurrent = maxInt(maxCurrent+n, n)
		maxGlobal = maxInt(max_Global, max_Current)
	}

	return maxGlobal
}

func maxInt(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}