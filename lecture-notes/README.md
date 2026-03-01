# Lecture Notes 📚

This directory contains the theoretical foundations and lecture notes necessary to tackle the algorithmic challenges in this repository.

The book explores fundamental data structures (Arrays, Linked Lists, Stacks, Queues, Trees, Heaps) and core algorithms (Binary Search, Sorting) along with common patterns.

## Building the eBook

The lecture notes are written using [Typst](https://typst.app/), a modern, fast, and highly-capable typesetting system.

### Prerequisites

You need to have `typst` installed on your system.

- You can download it from their [GitHub Releases](https://github.com/typst/typst/releases) or use a package manager:

  ```bash
  # macOS
  brew install typst
  
  # Windows (via winget)
  winget install --id Typst.Typst
  
  # generic cargo (Rust)
  cargo install --locked typst-cli
  ```

### Compiling to PDF

To generate the `lecture_notes.pdf` file, run the following command from this directory:

```bash
typst compile lecture_notes.typ lecture_notes.pdf
```

The resulting PDF will be generated instantly and feature a beautiful, typeset layout using the `min-book` template.
