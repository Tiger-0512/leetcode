func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	m := len(obstacleGrid)
	n := len(obstacleGrid[0])

	dp := make([][]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([]int, n)
	}
	dp[0][0] = 1

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if obstacleGrid[i][j] == 1 {
				dp[i][j] = 0
			} else {
				if i > 0 {
					dp[i][j] += dp[i-1][j]
				}
				if j > 0 {
					dp[i][j] += dp[i][j-1]
				}
			}
		}
	}

	return dp[m-1][n-1]
}