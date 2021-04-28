func permute(nums []int) [][]int {
	var results [][]int
	var permutation []int

	find_permutations(nums, permutation, &results)
	return results
}

func find_permutations(nums []int, permutation []int, results *[][]int) {
	if len(nums) == 0 {
		*results = append(*results, permutation)
		return
	}

	for i, n := range nums {
		find_permutations(
			append(append([]int{}, nums[:i]...), nums[(i+1):]...),
			append(permutation, n),
			results,
		)
	}
}