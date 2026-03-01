#import "@preview/min-book:0.1.1": (
  book, note, horizontalrule, hr, blockquote, appendices, annexes
)

#show: book.with(
  title: "Lecture Notes",
  subtitle: "Coding Interview Practice Foundations",
  authors: "Virtual Judge System Contributor",
  date: (2025, 03, 01),
  part: "Data Structures",
  chapter: "Topic",
)

= Basics

#include "chapters/01-introduction.typ"

#pagebreak()

= Linear Structures

#include "chapters/02-arrays.typ"

#include "chapters/03-linked-lists.typ"

#include "chapters/04-stacks-queues.typ"

#pagebreak()

= Hierarchical Structures

#include "chapters/05-trees.typ"

#include "chapters/06-heaps.typ"

#pagebreak()

= Algorithms

#include "chapters/07-binary-search.typ"

#include "chapters/08-sorting.typ"