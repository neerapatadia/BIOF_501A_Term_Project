"""
Project: BIOF 501 Term Project
Author: Neera Patadia

Description:
Script was used to take input NCBI fasta files, and clean then so the fasta
sequence is on a single line.

Input File:
NCBI fasta file containing gene sequences represented as nucleotides

Output File:
NCBI fasta file, where sequene is not split over multiple lines. Output files
save to the /outputs director

Running Instructions:
python3 clean_ncbi_fasta.py <input_file_name> <output_file_name>

"""
import os
import sys
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Align import MultipleSeqAlignment
from Bio.Align.Applications import MuscleCommandline
import subprocess

input_file = sys.argv[1]
output_file = sys.argv[2]

input_sequences = open(input_file, "r")
output_sequences = open(output_file, "w")


fasta_sequences = {}
lable = []
sequence = []
for line in input_sequences:
    if line.startswith(">"):
        line = line.strip("\n")
        lable.append(line)
    elif (line.startswith("A") or line.startswith("C") or line.startswith("G") or line.startswith("T")):
        line = line.strip("\n")
        sequence.append(line)
    elif line.startswith("\n"):
        sequence_string = ''.join(sequence)
        fasta_sequences[lable[0]]=sequence_string
        lable = []
        sequence = []

for item in fasta_sequences:
    output_sequences.write( item + "\n" + fasta_sequences[item] + "\n")
