# Find PAM

Find PAM sequence for CRISPR

## Description

It can read the FASTA file and find all of PAM, print out 20 nucleotides before PAM sequences, these sequences can be used at CRISPR guide RNA design. This python file can find out the CRISPR cleavage site of the bacteria, because most bacterial have PAM sequence as "NGG" (N is just any nucleotide).

## Introduction

![](PAM%20and%20gRNA.png)
CRISPR-Cas9 is a genome editing technology. In this system, the endonuclease Cas9 generates double strand breaks in DNA upon RNA-guided recognition of a complementary DNA sequence, which strictly requires the presence of a protospacer adjacent motif (PAM) next to the target site. Clustered Regularly Interspaced Short Palindromic Repeats (CRISPR) is a specific sequence in bacterial. The CRISPR-Cas system is a prokaryotic immune system that confers resistance to foreign genetic elements such as those present within plasmids and phages that provides a form of acquired immunity. In the DNA sequence of the phage, there is a small segment of the PAM gene, which is generally 2-6 bases in length. Cas1 and Cas2 will recognize the PAM gene and cut them, inserting this gene into the CRISPR gene of bacteria. It is like a new memory for bacterial gene. This PAM sequence is an important signal used by the Cas protein to identify "friends" and "enemies". When we use CRISPR for gene editing, we need to find PAM first, and design complementary sequences based on the first 20 bases of the PAM sequence to construct gudie RNA.

## How to use it

You can just download the FASTA what you want and change the file name as "sequence.fasta", then open the the python file, run it. It will output all of CRISPR editing point in python and save these information in a text file. The texe file's name is "Guide Sequences". Or you can change line 68 "filename" in the python file to the FASTA file you want to execute.

You can also import findpam into other python file.

### Example

I use findpam.py to read a FASTA file which is >NC_012692.1:118600-120237 Escherichia coli plasmid pAR060302 and the out put is the file "Guide Sequences".
The output is too long that it is not convient to show it in Readme.md, please go to Guide Sequences.txt if you want check the output.

## What I used

There is no need to import any biopython in this python file. I used a "class" to read the FASTA file, it can read the title and sequence in a "list" way. I then converted "list" to "string" for the following steps. Since I considered that some FASTA files may contain multiple-end sequences, I linked all the sequences in the "read_fasta_base" function.

Then I used some define to locate the "GG" in the sequence, and then printed the 20 nucleotides before the "GG" one by one.

## Version control

https://github.com/TetoSparrow/Find-PAM-for-CRISPR
You can see more details in "git" file.

## Future update

Some Improvements that will be implemented in the future are: 

1.Calculate the GC content of the first "20" nucleotides of the PAM sequence, as CRISPR gene editing is only possible when the "GC" content is between 40% and 80%.

2.Shows the specific position of the first twenty nucleotides of the PAM sequence in the FASTA file, such as from which base to which base.

3.Make a window where you can directly enter the file name to read the FASTA file directly.

## Versioning

Python 3.7

## Authors

Jinhui Gong
