#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 15:05:27 2019

@author: pedrod
"""
import sys
import os
import getopt
from Bio import Entrez
from Bio import SeqIO
from tqdm import tqdm


def downl(x, y, c, d, e):
    filename = x
    if not os.path.isfile(filename):
        net_handle = Entrez.efetch(db=c, id=y, rettype=d, retmode=e)
        out_handle = open(filename, "w")
        out_handle.write(net_handle.read())
        out_handle.close()
        net_handle.close()

def usage():
    print("THIS IS A TEST TO GET THE OPTION ON THE MAI PROGRAM")
    print("        -h prints the instructions ")
    print("        -d Type the desired database (in this test we use the nucleotide)")
    print('        -i the acessing number of the file')
    print('        -I File containing the acessing numbers of multiple files')
    print('        -n Name of the organism')
    print('        -N File containign the name of multiple organinsms')
    print('        -m User Entrez Mail (Necessary for downloading)')
    print('        -t The type of data that will be downloaded')
    print('        -r The type that the data will be saved')


def main(argv):
    dbf=str
    ida=''
    idf=''
    rett=str
    retm=str
    mail=str
    nm=str
    nf=''
    try:
        opts, args = getopt.getopt(argv, 'hi:I:t:r:m:n:N:d:')
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt == '-i':
            ida=str(arg)
        elif opt == '-I':
            print(arg)
            idf=arg
        elif opt == '-d':
            dbf=str(arg)
        elif opt == '-t':
            rett=str(arg)
        elif opt == '-r':
            retm=str(arg)
        elif opt == 'm':
            mail=str(arg)
        elif opt == '-n':
            nm=str(arg)
        elif opt == '-N':
            nf=arg
    if nf != '' and idf != '' and nm == '' and ida == '':
        print('starting the download of the files')
        Entrez.email = mail
        with open(nf) as f:
            content = f.read().splitlines()
        with open(idf) as f:
            content2 = f.read().splitlines()    
        for i in tqdm(range(len(content2))):
            x = content[i]+'.',retm
            y = content2[i]
            downl(x, y, dbf, rett, retm)
        print("COMPLETE")
    elif nf != '' and nm != '':
        print('Only one option can be used')
        usage()
        sys.exit(2)
    elif idf != '' and ida != '':
        print('Only one option can be used')
        usage()
        sys.exit(2)
    elif nm != '' and ida != '' and nf == '' and idf == '':
        x = nm+'.',retm
        y = ida
        downl(x, y, dbf, rett, retm)
        
if __name__=="__main__":
    main(sys.argv[1:])
