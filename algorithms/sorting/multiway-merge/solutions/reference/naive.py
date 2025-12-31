class FlatSortMerger:
    """Flatten all lists, then sort."""

    def kWayMerge(self, list_of_lists):
        combined = []
        for lst in list_of_lists:
            combined.extend(lst)
        return sorted(combined)
