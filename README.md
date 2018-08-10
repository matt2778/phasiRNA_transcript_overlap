# phasiRNA_transcript_overlap

Scripts for finding phasiRNAs overlapping transcripts in barley

## Function

These scripts were created to identify phasiRNA loci in the barley genome that overlap with
known barley protein coding transcripts.  The six different "parts" refer to the different regions
surrounding and including the transcript:

`Part 1:	Find phasiRNA loci 1kb upstream of transcript start site (not including start site in query)`  
`Part 2:	Find phasiRNA loci overlapping with transcript start site`  
`Part 3:	Find phasiRNA loci overlapping in transcript location`  
`Part 4:	Find phasiRNA loci overlapping with transcript stop site`  
`Part 5:	Find phasiRNA loci within 1Kb downstream of transcript stop site (not including stop site in query)`  
`Part 6:	Find phasiRNA loci in the full range of 1Kb upstream to 1Kb downstream`  

## Input Files

The two input files for this script include a csv file with phasiRNA location information and a text 
file with transcript location information

The phasiRNA csv location file format (separated by commas) is shown below:

`chromosome	phasiStart	phasiStop`
`chr1H	11528628	11528852`  
`chr1H	13134369	13134598`  
`chr1H	13134570	13134776`  
`chr1H	13134578	13134797`  
`chr1H	13965436	13965685`  
`chr1H	13977223	13977447`  
`chr1H	14300062	14300286`  
`chr1H	17316777	17317001`  
`chr1H	19369009	19369283`  

The transcript txt location file format is shown below:

`chr1H transcript 41811 45049 HORVU1Hr1G000010`  
`chr1H transcript 41959 44817 HORVU1Hr1G000010`  
`chr1H transcript 41961 45310 HORVU1Hr1G000010`  
`chr1H transcript 41963 44208 HORVU1Hr1G000010`  
`chr1H transcript 42077 44251 HORVU1Hr1G000010`  
`chr1H transcript 42077 44251 HORVU1Hr1G000010`  
`chr1H transcript 42161 44260 HORVU1Hr1G000010`  
`chr1H transcript 42655 44269 HORVU1Hr1G000010`  
`chr1H transcript 47106 50653 HORVU1Hr1G000020`  
`chr1H transcript 47707 48242 HORVU1Hr1G000020`  

## Output File

The output file includes transcripts with phasiRNA overlaps in the following format:

`chr1H transcript 19369458 19370979 HORVU1Hr1G008810`  
`chr1H transcript 19369490 19370926 HORVU1Hr1G008810`  
`chr1H transcript 19369578 19370912 HORVU1Hr1G008810`  
`chr1H transcript 19369673 19370911 HORVU1Hr1G008810`  
`chr1H transcript 19369693 19370938 HORVU1Hr1G008810`  
`chr1H transcript 29359977 29361653 HORVU1Hr1G011930`  
`chr1H transcript 29359980 29361633 HORVU1Hr1G011930`  
`chr1H transcript 40455673 40459820 HORVU1Hr1G014580`  
`chr1H transcript 59535232 59537207 HORVU1Hr1G017470`  
`chr1H transcript 59535303 59537654 HORVU1Hr1G017470`  
