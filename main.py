import os
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "pedrohenriquedornele@gmail.com"  # Always tell NCBI who you are


def downl(x, y, siz, sub):
    filename = x
    if not os.path.isfile(filename):
        # Downloading...
        net_handle = Entrez.efetch(db="nucleotide", id=y, rettype="fasta", retmode="fasta")
        out_handle = open(filename, "w")
        out_handle.write(net_handle.read())
        out_handle.close()
        net_handle.close()
        print(filename, " Saved")
        print(siz - sub, " remaining")
    else:
        print(filename, " alredy saved")
        print(siz - sub, " remaining")
    #print("Parsing...")



with open("100names") as f:
    content = f.read().splitlines()

with open("100lines") as f:
    content2 = f.read().splitlines()

for i in range(len(content2)):
    x = content[i]+".fasta"
    y = content2[i]
    siz = len(content2)
    sub = i+1
    downl(x, y, siz, sub)
