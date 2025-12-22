# Find Crossover Indices

## Problem Statement

You are given data that consists of points $(x_0, y_0), \ldots, (x_n, y_n)$, wherein $x_0 < x_1 < \ldots < x_n $, and  $y_0 < y_1 \ldots < y_n$ as well.

Furthermore, it is given that $y_0 < x_0$ and $ y_n > x_n$.

Find a "cross-over" index $i$ between $0$ and $n-1$ such that  $ y_i \leq x_i$ and $y_{i+1} > x_{i+1}$.

Note that such an index must always exist.

## Example

$$\begin{array}{c| c c c c c c c c c }
i & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\hline
x_i & 0 & 2 & 4 & 5 & 6 & 7 & 8 & 10 \\
y_i & -2 & 0 & 2 & 4 & 7 & 8 & 10 & 12 \\
\end{array} $$

Your algorithm must find the index $i=3$ as the crossover point ($x_3=5, y_3=4 \rightarrow y_3 \le x_3$ and $x_4=6, y_4=7 \rightarrow y_4 > x_4$).

## Complexity

The algorithm runs in $O(\log n)$ time complexity using a modified binary search approach.
