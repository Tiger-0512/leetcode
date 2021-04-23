func search(nums []int, target int) int {
	left, right := 0, len(nums)-1
	var mid int

	for left < right {
		mid = (left + right) / 2

		if nums[mid] > nums[right] {
			left = mid + 1
		} else {
			right = mid
		}
	}
	pivot := left

	left, right = 0, len(nums)-1

	if pivot == 0 {
		// pass
	} else if nums[0] <= target && target <= nums[pivot-1] {
		right = pivot - 1
	} else {
		left = pivot
	}

	for left <= right {
		mid = (left + right) / 2

		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return -1
}