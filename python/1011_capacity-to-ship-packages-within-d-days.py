class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        min_num = max(weights)
        max_num = sum(weights)

        while min_num < max_num:
            mid = (min_num + max_num) // 2
            days_required = 1
            current = 0

            for w in weights:
                current += w

                if current > mid:
                    days_required += 1
                    current = w

            if days_required <= D:
                max_num = mid
            else:
                min_num = mid + 1

        return min_num