
class PairwiseMergeKWay:
    """Pairwise merge with recursive reduction to a single list."""

    def kWayMerge(self, list_of_lists):
        k = len(list_of_lists)
        if k == 0:
            return []
        if k == 1:
            return list_of_lists[0]
        return self.kWayMerge(self._one_step(list_of_lists))

    def _one_step(self, list_of_lists):
        if len(list_of_lists) <= 1:
            return list_of_lists
        merged_lists = []
        k = len(list_of_lists)
        for i in range(0, k, 2):
            if i < k - 1:
                merged_lists.append(self._merge_two(list_of_lists[i], list_of_lists[i + 1]))
            else:
                merged_lists.append(list_of_lists[k - 1])
        return merged_lists

    def _merge_two(self, lst1, lst2):
        i = 0
        j = 0
        merged = []

        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                merged.append(lst1[i])
                i += 1
            else:
                merged.append(lst2[j])
                j += 1

        if i < len(lst1):
            merged.extend(lst1[i:])
        if j < len(lst2):
            merged.extend(lst2[j:])
        return merged
