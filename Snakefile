rule clean_ncbi_fasta:
    input:
        "example_input_files/TP53_refseq_transcript.fasta"
    output:
        "outputs/TP53_cleaned.fasta"
    shell:
        "python3 clean_ncbi_fasta.py {input} {output}"

rule calculate_gc_content:
    input:
        "outputs/TP53_cleaned.fasta"
    output:
        "outputs/gc_content_sequence_TP53.txt",
        gc_figure = "outputs/figures/gc_content/TP53_gc_content.pdf"
    shell:
        "python3 calculate_gc_content.py {input} {output} {output.gc_figure}"


rule perform_muscle_alignment:
    input:
        "outputs/TP53_cleaned.fasta"
    output:
        "outputs/TP53_msa.aln"
    shell:
        "python3 run_msa.py {input} {output}"

rule make_phylogenetic_tree:
    input:
        "outputs/TP53_msa.aln"
    output:
        "outputs/figures/trees/TP53_tree.pdf",
        tree_newick = "outputs/TP53_tree.nwk"
    shell:
        "python3 make_phylo_tree.py {input} {output.tree_newick} {output}"

rule make_seq_logo:
    input:
        file = "outputs/TP53_msa.aln"
    output:
        out = "outputs/figures/seq_logos/TP53_seq_logo.pdf"
    shell:
        "python3 make_pwm.py {input.file} {output.out} 3010 3020"
