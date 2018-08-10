#!/usr/bin/env python
#   This script will take a text file with chromosome info (chromosome, phasiStart, phasiStop) and pull out overlaping transcripts from
#   A transcript csv file

#   This version will include phasiRNA loci 1kb upstream of transcript start site (not including start site in query)

from sys import argv

script, target_directory, input_phasiRNA_location_file_csv, input_transcriptome_txt, output_file = argv

import os
os.chdir(target_directory)

import pandas as pd
import numpy as np

df = pd.read_csv(input_phasiRNA_location_file_csv)
df.head()

foo = ''
with open (input_transcriptome_txt) as transLoc:
    for line in transLoc:
        chrom = line.split()[0]
        transStart = int(line.split()[2])
        transStop = transStart -1
        transStart = transStart -1000
        bar = df.loc[(df['chromosome']==chrom) & (df['phasiStart']>=transStart) & (df['phasiStop']<=transStop)]
        if bar.empty:
            continue
        else:
            foo = foo + line
        print(foo)
        #print(bar)
        
with open (output_file, "w") as out_file:
    out_file.write(foo)