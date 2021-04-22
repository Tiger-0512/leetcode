class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == ['']:
            return [['']]

        table = collections.defaultdict(list)

        for s in strs:
            table[tuple(sorted(s))].append(s)

        return list(table.values())