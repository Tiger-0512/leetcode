func groupAnagrams(strs []string) [][]string {
	dict := make(map[string][]string)
	var ans [][]string

	for _, s := range strs {
		key := sortString(s)
		dict[key] = append(dict[key], s)
	}

	for _, s_list := range dict {
		ans = append(ans, s_list)
	}

	return ans
}

func sortString(s string) string {
	runes := []rune(s)
	sort.Slice(runes, func(a, b int) bool {
		return runes[a] < runes[b]
	})

	return string(runes)
}