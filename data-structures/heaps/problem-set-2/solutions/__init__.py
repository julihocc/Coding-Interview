"""
Solutions for Problem Set 2: Basic Datastructures and Heaps

This package exports the following data structures:
- MinHeap: Min-heap implementation (from problem1_minheap)
- TopKHeap: Maintain k smallest elements (from problem1_topk)
- MaxHeap: Max-heap implementation (from problem2_maxheap)
- MedianMaintainingHeap: Efficient median computation (from problem2_median)
"""

from .problem1_minheap import MinHeap
from .problem1_topk import TopKHeap
from .problem2_maxheap import MaxHeap
from .problem2_median import MedianMaintainingHeap

__all__ = ['MinHeap', 'TopKHeap', 'MaxHeap', 'MedianMaintainingHeap']
