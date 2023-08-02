This projects aims to develop a tool with a simple user interface for sequence (fastq and fasta) files analysis.

While it works on other kind of files, its behavior is unprecise and not recommended.

This script works with two main functions: 
1. Conversion from FASTQ to FASTA - This option takes a file fastq as input and 
creates a new fasta file with header and sequence; 
2. ORFs finding and translation - From a nucleotide fasta file, 
finds the ORFs in it and writes them in a separate fasta_orf file and the same time, writes the translated sequence 
in a new file.

The user interface is quite simple and has a file selector and a running button for the two functions.
