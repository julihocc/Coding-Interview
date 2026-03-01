#import "@preview/ilm:1.4.0": *

#show: ilm.with(
  title: [Lecture Notes],
  author: "Virtual Judge System Contributor",
  date: datetime(year: 2025, month: 3, day: 1),
  abstract: [
    A cohesive guide to the theoretical foundations necessary to tackle algorithmic challenges in modern coding interviews. Covers data structures, algorithms, and complexity analysis.
  ],
  paper-size: "a4",
)

= Introduction

#include "chapters/01-introduction.typ"

= Data Structures

#include "chapters/02-arrays.typ"

#include "chapters/03-linked-lists.typ"

#include "chapters/04-stacks-queues.typ"

#include "chapters/05-trees.typ"

#include "chapters/06-heaps.typ"

= Algorithms

#include "chapters/07-binary-search.typ"

#include "chapters/08-sorting.typ"
