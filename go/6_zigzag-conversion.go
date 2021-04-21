import (
	"strings"
)

func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}

	s_list := make([]string, numRows)
	step := 1
	pos := 0

	for i := 0; i < len(s); i++ {
		s_list[pos] += string(s[i])
		pos += step

		if pos == 0 || pos == numRows-1 {
			step *= -1
		}
	}

	ans := strings.Join(s_list, "")
	return ans
}