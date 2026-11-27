# Multi-Line FASTA Sequence Analyzer

A lightweight command-line bioinformatics tool written in pure Python to parse multi-line FASTA files and compute sequence metrics without external dependencies.

## Features
- Parses single-line and multi-line FASTA files while ignoring blank lines and preserving empty sequence records.
- Handles headerless sequence data gracefully without crashing.
- Calculates sequence length, GC content percentage, individual nucleotide counts (`A`, `T`, `G`, `C`), and standard stop codon counts (`TAA`, `TAG`, `TGA`) in the first reading frame.
- Exports results to a clean tab-separated values (`.tsv`) report.

## Usage

Run the script from your terminal by passing an input FASTA file and an optional output filename (defaults to `summary.tsv`):

```bash
python fasta_analyzer.py <input.fasta> [output.tsv]