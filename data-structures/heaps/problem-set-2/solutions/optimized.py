"""Optimized solutions for heaps problem-set-2.

This module reuses the optimized heap implementations from heaps.py.
The implementations are already optimized for:
  - MinHeap/MaxHeap: O(log n) operations with iterative bubble operations
  - TopKHeap: O(k) insertion with efficient merge
  - MedianMaintainingHeap: O(log n) insertion with balanced heaps
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from heaps import MinHeap, MaxHeap, TopKHeap, MedianMaintainingHeap


def solve():
    """Test runner validating all optimized heap implementations."""
    
    # Test MinHeap
    h = MinHeap()
    h.insert(5); assert h.min_element()==5
    h.insert(2); assert h.min_element()==2
    h.insert(4); assert h.min_element()==2
    h.insert(-1); assert h.min_element()==-1
    h.insert(7); assert h.min_element()==-1
    h.delete_min(); assert h.min_element()==2
    h.delete_min(); assert h.min_element()==4
    h.delete_min(); assert h.min_element()==5
    h.delete_min(); assert h.min_element()==7
    h.delete_min(); assert h.size()==0
    
    # Test MaxHeap
    h = MaxHeap()
    h.insert(5); assert h.max_element()==5
    h.insert(2); assert h.max_element()==5
    h.insert(4); assert h.max_element()==5
    h.insert(-1); assert h.max_element()==5
    h.insert(7); assert h.max_element()==7
    h.delete_max(); assert h.max_element()==5
    h.delete_max(); assert h.max_element()==4
    h.delete_max(); assert h.max_element()==2
    h.delete_max(); assert h.max_element()==-1
    h.delete_max(); assert h.size()==0
    
    # Test TopKHeap
    tk = TopKHeap(3)
    for x in [7, 5, 3, 8, 1, 9, 2]:
        tk.insert(x)
    assert tk.A == [1, 2, 3], f"Expected [1, 2, 3], got {tk.A}"
    
    # Test MedianMaintainingHeap
    mh = MedianMaintainingHeap()
    mh.insert(1); assert mh.get_median() == 1
    mh.insert(2); assert mh.get_median() == 1.5
    mh.insert(3); assert mh.get_median() == 2
    mh.insert(4); assert mh.get_median() == 2.5
    mh.insert(5); assert mh.get_median() == 3
    
    return True
