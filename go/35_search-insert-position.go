func searchInsert(nums []int, target int) int {
	left, right := 0, len(nums)-1
	var mid int

	for left <= right {
		mid = (left + right) / 2

		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			left = mid + 1
		} else { // target < nums[mid]
			right = mid - 1
		}
	}
	return left
}