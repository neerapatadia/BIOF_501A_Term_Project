import os
import matplotlib.pyplot as plt
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
output_figure = sys.argv[3]

input = open(input_file, "r")
output = open(output_file, "w")

output.write("Name" + "\t" + "GC_Content" + "\n")

sequence_gc_content = {}
lable = []
gc_content = []

for line in input:
    if line.startswith(">"):
        line = line.strip("\n")
        lable.append(line)
    else:
        sequence_string = line.strip("\n")
        total_chars = len(sequence_string)
        a_content = sequence_string.count("A")
        t_content = sequence_string.count("T")
        c_content = sequence_string.count("C")
        g_content = sequence_string.count("C")
        gc_sum = g_content + c_content
        gc_content_value = gc_sum/total_chars
        gc_content.append(gc_content_value)

for item in lable:
    print(item)
    i = lable.index(item)
    output.write(item + "\t" + str(gc_content[i]) + "\n")

plt.bar(lable,gc_content)
plt.xlabel('FASTA Sequence Labels')
plt.ylabel('GC Content Calculated')
plt.title('GC Content Distribution')
plt.savefig(output_figure)
plt.show()
