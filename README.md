### Note from 2015

This is a little program I wrote while I was still working at Dr. Tsang's biochemistry lab on a summer fellowship at University of Cincinnati.
I think they Sparky NMR analysis project is abandoned at this point but this script may still be useful for somebody but honestly 
you could do the same thing with a spreadsheet program. 

I am now a software engineer fulltime and not involved in Chemistry much any more and I have come a long way as programmer since I wrote this rudimentary script.

As a side note [a paper did come out of this](http://www.ncbi.nlm.nih.gov/pubmed/23065336).


### Intro:

This is a small script that deals with NMR chemical shift analysis 
for gross structure comparison in proteins. The shifts determined experimentally
are compared to the shifts from the references, if it above the listed range the 
amino acid corresponding receives a 1, if it within the range, it recieves a 0,
if it is below, it recieves a -1. 

If there is a pattern of 1's or -1's for more than 4 sequential amino acids, this may
indicate some secondary structure. Agreement between multiple atoms should
correlate if this is accurate.


See the 1994 Wishart paper for background:

	Title:The 13C Chemical-Shift Index: A simple method for the
	identification of protein secondary structure using 13C chemical-shift data*          
	Authors: DavidS.Wishart and BrianD.Sykes**
	Pub: Journal of Biomolecular NMR, 4 (1994) 171-180


Notes:
	results directory:
	Processed Data from Sparky format input.
	
	shifts-ref directory:
	The references for the coiled shifts from the 1994 paper. These were
	provided with the original program developed by Wishart, written in C.
	
	shifts.py: the above noted references in python dict format
	
	
Example:
	Using shifts from N-Terminal of Human Lys-RS in Sparky format


