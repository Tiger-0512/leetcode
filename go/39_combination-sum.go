func combinationSum(candidates []int, target int) [][]int {
	dp := make([][][]int, target+1)
	dp[0] = [][]int{{}}

	sort.Slice(candidates, func(i, j int) bool {
		return candidates[i] < candidates[j]
	})

	for _, c := range candidates {
		for i := 0; i < target+1; i++ {
			if i >= c {
				for _, d := range dp[i-c] {
					tmp := make([]int, len(d))
					copy(tmp, d)
					tmp = append(tmp, c)
					dp[i] = append(dp[i], tmp)
				}
			}
		}
	}
	return dp[len(dp)-1]
}