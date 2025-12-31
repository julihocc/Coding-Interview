class FlatSortMerger:
    """Flatten all lists, then sort."""

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def kWayMerge(self):
        combined = []
        for lst in self.list_of_lists:
            combined.extend(lst)
        return sorted(combined)
