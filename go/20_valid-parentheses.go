type strStack []string

// Implementation of Stack
func (stack *strStack) push(s string) {
	*stack = append(*stack, s)
}
func (stack *strStack) pop() string {
	result := (*stack)[len(*stack)-1]
	*stack = (*stack)[:(len(*stack) - 1)]
	return result
}
func (stack *strStack) isEmpty() bool {
	if len(*stack) == 0 {
		return true
	}
	return false
}

// Judge whether the stack contains "{", "(" or "["
func contain(s string, dict map[string]string) bool {
	for index := range dict {
		if s == index {
			return true
		}
	}
	return false
}

func isValid(s string) bool {
	dict := map[string]string{"(": ")", "{": "}", "[": "]"}
	var stack strStack = make([]string, 0)

	for _, char := range s {
		if contain(string(char), dict) == true {
			stack.push(string(char))
		} else {
			if stack.isEmpty() == true {
				return false
			}
			tmp := stack.pop()
			if dict[tmp] != string(char) {
				return false
			}
		}
	}
	if stack.isEmpty() == true {
		return true
	}
	return false
}