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

Gene Sequence Analyzer consists of 5 python files, and a snakemake file. Each python script carried out a different part of the Gene Sequence Analyzer pipline, and are described below:

1. clean_ncbi_fasta.py: takes an input NCBI refseq fasta file, and reformats so nucleotide sequence takes up a single line, as opposed to being split over multiple lines.
2. run_msa.py: takes the cleaned NCBI fasta file and runs a MUSCLE alignment to output an alignment file in MUSCLE format
3. calculate_gc_content.py: computes gc content of each sequence based on the aligned .fasta file
4. make_phylo_tree.py: makes a phylogenetic tree based on the multiple sequence alignment program output
5. make_pwm.py: takes a specific section of the multiple sequence alignment and computes a position weight matrix, which is used to generate a sequence logo. 

All of these files can be run through the snakemake file using the running instructions outlined below. 
Input fasta sequence files can be downloaded from: https://www.ncbi.nlm.nih.gov/gene/7157/ortholog/?scope=117570&term=TP53
Search a gene of interest, and select orthologs. Click on the species of interest and hit download. On the drop down menu, selection "one sequence per gene".


**Running Instructions**
Please note that this program was intended to be run on a MacOSX/Unix environment.

To run the program, you will be required to instatiate a conda environment, install snakemake, and will need to have the required rependencies installed. To set up a conda environment, run the following command in the commandprompt/terminal:

```
conda activate base
mamba create -c conda-forge -c bioconda -n snakemake snakemake
```

next you will need to install the dependencies which can be done using the pip command

```
pip install biopython
pip install pathlib
pip install logomaker
pip install matplotlib
pip install Bio.Align.Applications
pip install Bio.Align
pip install Bio
pip install pandas
pip install Bio.SeqRecord
pip install Bio.SeqIO
pip install Bio.Align
pip install pylab
pip install Graphviz
pip install Bio.Phylo.TreeConstruction
```

From the ```/BIOF_501A_Term_Project``` we can use the snakemake file to run the program. 

To clean and pre-process the fasta file, use the following command (You will need to specify the gene name in all caps.):
```
snakemake outputs/{gene_name}_cleaned.fasta --cores 1
```

To run the multiple sequence alignment use the following command (replace the term in the {} with the desired value):
```
snakemake example_input_files/{gene_name}_refseq_transcript.fasta --cores 1
```

To calculate the gc content (this will also generate the barplot figure):
```
snakemake outputs/gc_content_sequence_{gene_name}.txt --cores 1
```

To generate the phylogenetic tree and corresponding newick file:
```
snakemake outputs/figures/trees/{gene_name}_tree.pdf --cores 1
```

To generate the sequence logos, use the following command (you will need to specify the start and end position of the part of the MSA you would like to be analysed in the {start} and {end} values): 

```
snakemake outputs/figures/seq_logos/{gene_name}_seq_logo_{start}_{end}.pdf --cores 1
```

all output files will be saved to the ```outputs``` folder, and can be compared by looking at the files in ```example outputs```. 


**References**
1. Edgar R. C. (2004). MUSCLE: multiple sequence alignment with high accuracy and high throughput. Nucleic acids research, 32(5), 1792–1797. https://doi.org/10.1093/nar/gkh340
2. ŠMarda, P., Bureš, P., Horová, L., Leitch, I. J., Mucina, L., Pacini, E., Tichý, L., Grulich, V., & Rotreklová, O. (2014). Ecological and evolutionary significance of genomic GC content diversity in monocots. Proceedings of the National Academy of Sciences, 111(39), E4096–E4102. https://doi.org/10.1073/pnas.1321152111
3. Kim, J., Rosenberg, N. A., & Palacios, J. A. (2020). Distance metrics for ranked evolutionary trees. Proceedings of the National Academy of Sciences, 117(46), 28876–28886. https://doi.org/10.1073/pnas.1922851117
