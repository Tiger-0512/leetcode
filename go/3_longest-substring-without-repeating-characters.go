func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}

	dict := make(map[rune]int)
	var start float64 = 0
	var ans float64 = 0

	for i, c := range s {
		if dict[c] != 0 {
			start = math.Max(start, float64(dict[c]))
		}

		dict[c] = i + 1
		ans = math.Max(ans, float64(i-int(start)+1))
	}

	return int(ans)
}