from Bio import Phylo
from Bio import AlignIO
import matplotlib
import matplotlib.pyplot as plt
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import pylab
import sys


input_alignment = sys.argv[1]
output_tree_file = sys.argv[2]
output_tree_image = sys.argv[3]

align = AlignIO.read(input_alignment , "fasta")

calculator = DistanceCalculator("identity")
dist_mat = calculator.get_distance(align)

constructor = DistanceTreeConstructor()
tree = constructor.upgma(dist_mat)

for clade in tree.get_nonterminals():
    clade.name = ""

Phylo.write(tree, output_tree_file,"newick")

fig = plt.figure(figsize=(50,40), dpi = 100)
plt.rcParams.update({"font.size": 30 })
axes = fig.add_subplot(1,1,1)
fig1 = plt.gcf()
tree.ladderize()
Phylo.draw(tree, axes = axes, show_confidence = True, do_show = False)
plt.savefig(output_tree_image)
