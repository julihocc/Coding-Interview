# Multiway Merge

## Problem Statement

Merge `k` different sorted lists into a single sorted list.

## Algorithm

The algorithm implements a `k`-way merge by calling `twoWayMerge` repeatedly:

1. Call `twoWayMerge` on consecutive pairs of lists `twoWayMerge(lists[0], lists[1])`, ... , `twoWayMerge(lists[k-2], lists[k-1])`.
2. Thus, we create a new list of lists of size `k/2`.
3. Repeat steps until we have a single list left.

## Complexity

The overall running time of the algorithm is $\Theta(n k \log(k))$, where each list is size $n$ and there are $k$ lists.
