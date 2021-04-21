func nextPermutation(nums []int) {
	var j int

	for i := len(nums) - 2; i >= 0; i-- {
		if nums[i] < nums[i+1] {
			j = i
			break
		}
		if i == 0 {
			j = -1
		}
	}

	if j != -1 {
		for i := len(nums) - 1; i > j; i-- {
			if nums[i] > nums[j] {
				nums[j], nums[i] = nums[i], nums[j]
				break
			}
		}
	}

	for i := 0; i < len(nums[(j+1):])/2; i++ {
		nums[j+i+1], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[j+i+1]
	}
}