// Binary Search with Recursion
func findMin(nums []int) int {
	left, right := 0, len(nums)-1

	if nums[left] < nums[right] || len(nums) == 1 {
		return nums[0]
	}

	mid := int((left + right) / 2)

	if nums[right] < nums[mid] {
		return findMin(nums[(mid + 1):])
	} else {
		return findMin(nums[:(mid + 1)])
	}
}

/*---------------------------------------------------------------------------------------*/

// Simple Binary Search
func findMin(nums []int) int {
	left, right := 0, len(nums)-1

	for left < right {
		mid := int((left + right) / 2)

		if nums[right] < nums[mid] {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return nums[left]
}