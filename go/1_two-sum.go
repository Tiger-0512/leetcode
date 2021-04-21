func twoSum(nums []int, target int) (ans []int) {
	if len(nums) == 0 {
		return
	}

	dict := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		tmp := contains(dict, nums[i])
		if tmp != -1 {
			ans = append(ans, tmp)
			ans = append(ans, i)
			return
		} else {
			dict[i] = target - nums[i]
		}
	}
	return
}

func contains(dict map[int]int, num int) int {
	for i := 0; i < len(dict); i++ {
		if dict[i] == num {
			return i
		}
	}
	return -1
}