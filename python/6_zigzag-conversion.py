class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Check input
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialization
        s_list = [''] * numRows
        pos = 0
        step = 1

        for i, l in enumerate(s):
            s_list[pos] += l
            pos += step

            if pos == 0 or pos == numRows - 1:
                step *= -1

        ans = ''.join(s_list)

        return ans