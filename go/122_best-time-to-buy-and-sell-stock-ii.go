// Peak Valley Approach
func maxProfit(prices []int) int {
	valley, peak := prices[0], prices[0]
	ans := 0

	for i := 0; i < len(prices)-1; i++ {
		for i < len(prices)-1 && prices[i] >= prices[i+1] {
			i++
		}
		valley = prices[i]
		for i < len(prices)-1 && prices[i] <= prices[i+1] {
			i++
		}
		peak = prices[i]
		ans += peak - valley
	}
	return ans
}

/*---------------------------------------------------------------------------------------*/

// One Pass
func maxProfit(prices []int) int {
	ans := 0
	for i := 0; i < len(prices)-1; i++ {
		if prices[i] < prices[i+1] {
			ans += prices[i+1] - prices[i]
		}
	}
	return ans
}