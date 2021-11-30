"""
Project: BIOF 501 Term Project
Author: Neera Patadia

Description:
Performs multiple sequence alignment on input fasta sequences using the
MUSCLE alignment algorithm.

Input File:
Cleaned NCBI fasta file

Output File:
NCBI fasta file, where sequene is not split over multiple lines. Output files
save to the /outputs directory.

Running Instructions:
python3 clean_ncbi_fasta.py <input_file_name> <output_file_name>
"""
import sys,os, subprocess
from Bio import AlignIO
from Bio.Align.Applications import MuscleCommandline

input_file = sys.argv[1]
output_file = sys.argv[2]

muscle_exe = "muscle"
out_file = output_file


def run_muscle_alignment():
    muscle_cline = MuscleCommandline(muscle_exe, input=input_file, out = out_file, maxiters = 2, diags= True)
    stdout, stderr = muscle_cline()
    MultipleSeqAlignment = AlignIO.read(out_file, "fasta")
    return(muscle_cline)

aln = run_muscle_alignment()




"""
quantitative as opposed to
framing around why we choose to do certain things
ordered with three and then a weird one, non-sequential selection on purpose
senario needs to be more clear
diverging + extra to describe colour scheme
"radial panning/scrolling"
in writeup --> how many visualizations need to be looked at
scale of data versus scale of visualization
scales of how many variants we would want --> tool to understand why we use certain thresholds
Need to look a variants --> want to visualize significantly more variants as opposed to just a small number of them
talk about how we can go from huge set of data to smaller set of data
"""
