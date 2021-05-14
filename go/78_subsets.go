func subsets(nums []int) [][]int {
	ans := [][]int{[]int{}}

	for _, n := range nums {
		for _, a := range ans {
			tmp := append(append([]int{}, a...), n)
			ans = append(ans, tmp)
		}
	}
	return ans
}