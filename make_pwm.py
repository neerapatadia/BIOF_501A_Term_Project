from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio.Seq import Seq
from Bio import SeqIO
import pandas as pd
import logomaker
import matplotlib.pyplot as plt
import sys
from pathlib import Path

input_file = sys.argv[1]
output_file = sys.argv[2]
#start_position = int(sys.argv[3])
#end_position = int(sys.argv[4])

f_name = Path(output_file).stem
f_name_list = f_name.split("_")
start_position = int(f_name_list[3])
end_position = int(f_name_list[4])

alignment = AlignIO.read(input_file, "fasta")
aln_len = alignment.get_alignment_length()

if start_position < 0 or start_position > aln_len:
    print("invalid start position - please try again with an appropriate value")
elif end_position < 0 or end_position > aln_len:
    print("invalid end position - please try again with an appropriate value")
elif end_position < start_position:
    print("end position is smaller than start postition, please try again with an appropriate value")

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
