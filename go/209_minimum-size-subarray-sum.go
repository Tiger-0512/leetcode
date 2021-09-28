// O(n) solution with Pointer
func minSubArrayLen(target int, nums []int) int {
    ans := len(nums) + 1
    left := 0
    sum := 0
    
    for i, n := range nums {
        sum += n
        for sum >= target {
            ans = min(ans, i-left+1)
            sum -= nums[left]
            left += 1
        }
    }
    if ans == len(nums) + 1 {
        return 0
    } else {
        return ans
    }
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

/*---------------------------------------------------------------------------------------*/

// O(nlogn) Solution with Binary Search
func minSubArrayLen(target int, nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    sums := make([]int, len(nums)+1)
    for i := 1; i < len(sums); i++ {
        sums[i] = sums[i - 1] + nums[i - 1]
    }
    
    ans := len(nums) + 1
    
    for i := 1; i < len(sums); i++ {
        if sums[i] >= target {
            left := binarySearch(0, i-1, sums[i]-target, sums)
            ans = min(ans, i-left)
        }
    }
    
    if ans == len(nums) + 1{
        return 0
    }
    return ans
}

func binarySearch(left, right, target int, sums []int) int {
    for left < right {
        mid := (left + right) / 2
        if sums[mid] < target {
            left = mid + 1
        } else {
            right = mid
        }
    }
    if sums[left] > target {
        return left - 1
    }
    return left
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

