from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio.Seq import Seq
from Bio import SeqIO
import pandas as pd
import logomaker
import matplotlib.pyplot as plt
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
start_position = int(sys.argv[3])
end_position = int(sys.argv[4])

alignment = AlignIO.read(input_file, "fasta")
selection = alignment[:, start_position:end_position]


def alnSiteCompositionDF(alignment, characters="ATCG"):
  alnRows = alignment.get_alignment_length()
  compDict = {char:[0]*alnRows for char in characters}
  for record in alignment:
    header = record.id
    seq = record.seq
    for ntPos in range(len(seq)):
      nt = seq[ntPos]
      if nt in characters:
        compDict[nt][ntPos] += 1
  return(pd.DataFrame.from_dict(compDict))

alignment_CompDF = alnSiteCompositionDF(selection)
alignment_FreqDF = alignment_CompDF.div(alignment_CompDF.sum(axis=1), axis=0)


logo = logomaker.Logo(alignment_FreqDF)
plt.savefig(output_file)
