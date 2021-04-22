class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        ans = []

        for i in nums1:
            set1.add(i)

        for j in nums2:
            if j in set1 and not j in ans:
                ans.append(j)

        return ans


#---------------------------------------------------------------------------------------#


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = dict()
        ans = []

        for i in nums1:
            dic1[i] = True

        for j in nums2:
            try:
                if dic1[j] == True and not j in ans:
                    ans.append(j)
            except:
                pass

        return ans
