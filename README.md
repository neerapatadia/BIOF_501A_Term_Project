# BIOF_501A_Term_Project - Gene Sequence Analyzer

![Test Image 4](https://github.com/neerapatadia/BIOF_501A_Term_Project/blob/main/images/Screen%20Shot%202021-12-01%20at%204.07.51%20PM.png)

A major goal in bioinformatics is to examine and compare gene sequences across multiple species. These types of analyses can provide insights into regions within a gene that are conserved across species. Typically, regions of the genome (and therefore within individual genes) are considered to be of functional significance, and important for the overall fitness to the organism. There are a variety of methods that can be used to examine gene sequences among multiple species. Specifically, phylogenetic analysis of gene sequences can provide evolutionary insights as to how gene sequenes are related to each other. Furthmore, sequence logos are another type of visualization of nucleotide composition that can be used to understand relationships between gene sequences of different species. Additionally, metrics such as GC content within a gene can provide insights into the overall quality of a given gene sequence.

In this project, I propose the use of Gene Sequence Analyzer. Gene Sequence Analyzer is a software package that takes a set of gene fasta sequences from multiple species, obtained by the NCBI Nucleotide databases, and aligns them using the MUSCLE alignment algorithm. Once the alignment as been performed, different types of analyses of the gene sequences can be performed. These analyses are described in the following table:

Analysis      | Description  | Input file | Output file(s)
------------- | -------------|------------|-------------
GC content of sequence  | for each sequence in an file consisting of a set of fasta gene sequences, the GC content is calculated and displayed on a bar chart.  | file containing fasta gene sequences of multiple species| table with fasta sequence lable and corresponding calculated GC content in .txt format and barplot of GC content per sequence in .pdf format
Construct Phylogenetic tree  | based on the sequence input, compute and visualize a phylogenetic tree based on a computed distance matrix.  | alignment file in MUSCLE format| newick tree file and .pdf file of phylogenetic tree visualization.
Compute Position Weight Matrix| calculate the position weight matrix based on a basepair section of the genes in the multiple sequence alignment. | alignment file in MUSCLE format | position weight matrix in .txt format
Generate Sequence Logos | generate a sequence logo based on the distance matrix. | postion weight matrix in .txt format| .pdf file containing the sequence logo image.

The workflow used to carry out this analysis can be visualized in the following snakemake workflow diagram:

![Test Image 5](https://github.com/neerapatadia/BIOF_501A_Term_Project/blob/main/images/dag.svg)


**Package Description**

Gene Sequence Analyzer consists of 5 python files, and a snakemake file. Each python script carried out a different part of the pipline 

**Running Instructions**

To run the program, you will be required to instatiate a conda environment, and will need to have the required rependencies installed.
