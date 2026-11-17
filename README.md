# Multi-Line FASTA Sequence Analyzer

A pure-Python bioinformatics command-line tool that parses raw multi-line FASTA sequence files, computes key nucleotide metrics, and outputs a structured tab-separated summary report (`.tsv`).

## Features
- **Multi-Line FASTA Parsing:** Streams sequence files line-by-line without loading entire genomes into memory, reconstructing fragmented sequences using a header state machine.
- **Sequence Metrics:** Calculates sequence length (bp), GC content percentage, individual base counts (`A`, `T`, `G`, `C`), and in-frame stop codon counts (`TAA`, `TAG`, `TGA`).
- **Tab-Separated Output:** Generates a clean `summary.tsv` report compatible with Excel and downstream `pandas` workflows.

## Project Structure
```text
fasta_project/
├── fasta_analyzer.py   # Core parsing, analysis, and reporting functions
├── samples.fasta       # Sample multi-line bacterial gene sequences
└── summary.tsv         # Generated sequence analysis report