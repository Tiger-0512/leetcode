func numIslands(grid [][]byte) int {
	m, n := len(grid), len(grid[0])
	ans := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == '1' {
				bfs(&grid, i, j)
				ans++
			}
		}
	}
	return ans
}

func bfs(grid *[][]byte, i, j int) {
	queue := [][]int{}
	queue = append(queue, []int{i, j})

	for len(queue) > 0 {
		_i, _j := queue[0][0], queue[0][1]
		queue = queue[1:]

		if _i < 0 || _j < 0 || _i > len(*grid)-1 || _j > len((*grid)[0])-1 || (*grid)[_i][_j] == '0' {
			continue
		}
		(*grid)[_i][_j] = '0'
		queue = append(queue, []int{_i - 1, _j})
		queue = append(queue, []int{_i + 1, _j})
		queue = append(queue, []int{_i, _j - 1})
		queue = append(queue, []int{_i, _j + 1})
	}
	return
}
