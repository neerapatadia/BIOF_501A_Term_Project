rule clean_ncbi_fasta:
    input:
        "example_input_files/{gene_name}_refseq_transcript.fasta"
    output:
        "outputs/{gene_name}_cleaned.fasta"
    shell:
        "python3 clean_ncbi_fasta.py {input} {output}"

rule calculate_gc_content:
    input:
        "outputs/{gene_name}_cleaned.fasta"
    output:
        "outputs/gc_content_sequence_{gene_name}.txt",
        gc_figure = "outputs/figures/gc_content/{gene_name}_gc_content.pdf"
    shell:
        "python3 calculate_gc_content.py {input} {output} {output.gc_figure}"

rule perform_muscle_alignment:
    input:
        "outputs/{gene_name}_cleaned.fasta"
    output:
        "outputs/{gene_name}_msa.aln"
    shell:
        "python3 run_msa.py {input} {output}"

rule make_phylogenetic_tree:
    input:
        "outputs/{gene_name}_msa.aln"
    output:
        "outputs/figures/trees/{gene_name}_tree.pdf",
        tree_newick = "outputs/{gene_name}_tree.nwk"
    shell:
        "python3 make_phylo_tree.py {input} {output.tree_newick} {output}"

rule make_seq_logo:
    input:
        "outputs/{gene_name}_msa.aln"
    output:
        out = "outputs/figures/seq_logos/{gene_name}_seq_logo_{start}_{end}.pdf"
    shell:
        "python3 make_pwm.py {input} {output.out}"
