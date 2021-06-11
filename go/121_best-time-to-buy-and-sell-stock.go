// One Pass
func maxProfit(prices []int) int {
	min, profit := prices[0], 0

	for _, p := range prices[1:] {
		if p < min {
			min = p
		}
		if p-min > profit {
			profit = p - min
		}
	}
	return profit
}

/*---------------------------------------------------------------------------------------*/

// Dynamic Programming
func maxProfit(prices []int) int {
	dp := [][]int{}
	dp = append(dp, []int{prices[0], 0})

	for i, p := range prices[1:] {
		dp = append(dp, []int{min(p, dp[i][0]), max(p-dp[i][0], dp[i][1])})
	}
	return dp[len(dp)-1][1]
}

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}
func max(a, b int) int {
	if a < b {
		return b
	} else {
		return a
	}
}