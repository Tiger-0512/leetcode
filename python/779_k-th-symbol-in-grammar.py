class Solution:
    def kthGrammar(self, N: int, K: int) -> int:

        def bin_tree(i, k, curr):
            mid = int((2 ** ((N - 1) - i)) / 2)

            if k == 1:
                return curr

            # Go left
            if k <= mid:
                if curr == 0:
                    return bin_tree(i + 1, k, 0)
                else:
                    return bin_tree(i + 1, k, 1)

            # Go right
            else:
                if curr == 0:
                    return bin_tree(i + 1, k - mid, 1)
                else:
                    return bin_tree(i + 1, k - mid, 0)

        return bin_tree(0, K, 0)