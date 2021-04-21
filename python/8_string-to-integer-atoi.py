class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        upper_bound = 2 ** 31 - 1
        lower_bound = -(upper_bound + 1)

        positive = True

        i = 0
        flag = 0
        ans = '0'

        while i <= len(s) - 1:
            if flag == 1:
                if s[i] == '0' and not ans:
                    i += 1
                elif '0' <= s[i] <= '9':
                    ans += s[i]
                    i += 1
                elif (s[i] == '+' or s[i] == '-') and (s[i - 1] == '+' or s[i - 1] == '-'):
                    return 0
                else:
                    break

            elif s[i] is ' ':
                s = s[(i + 1):]
            elif 'a' <= s[i] <= 'z' or s[i] == '.':
                return 0
            elif (s[i] == '+' or s[i] == '-') and len(s) == 1:
                return 0
            elif s[i] == '+':
                i += 1
                flag = 1
            elif s[i] == '-':
                positive = False
                i += 1
                flag = 1
            else:
                flag = 1

        while ans[0] == '0':
            if len(ans) == 1 and ans[0] == '0':
                return 0
            ans = ans[1:]
        if not positive:
            ans = '-' + ans
        if int(ans) > upper_bound:
            ans = upper_bound
        elif int(ans) < lower_bound:
            ans = lower_bound
        return ans