#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sparky CSI analyzer
#       
#       Copyright 2012 a-r-d ... Aaron Decker
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
import sys
import re
from shifts import *

#this will be a list of the atom types
column_headings = []
# c / C = colist
# ca / CA = calist
# cb / CB = cblist
# ha / HA = halist
other_lines = [] #all else

def read_input_file():
	print "Enter a file name: "
	#name = raw_input("> ")
	name = "rmnshifts-singlespace.txt"
	f = open(name, "r")	
	return f
	
def read_a_line(sfile):
	i = 0;
	while(1):
		line = sfile.readline()
		#print line
		if(i == 0):
			splitlist = line.split(' ')
			for x in splitlist:
				column_headings.append(x)
		else:
			other_lines.append(line)
		i += 1
		if line == "":
			break
	
	
def compare_single_index(filename,indexpos,indexlist):
	#note, 0th index in linesplit is nothing
	# 1 is aa type
	# 2 is CA 
	fileobj = open(filename, 'w')
	
	i = 1 # MISSING FIRST RESIDUE
	ii = 1
	number = 0
	for line in other_lines:
		
		if line: #NOT EMPTY string is false if empty
			splitlist = line.split(' ')
			if splitlist: #NOT EMPTY list is false if empty
				#Get the amino acid
				aa = splitlist[1]
				aa_first_letter = aa[0]
				# HOW TO CONVERT TO UPPERCASE, IF LOWERCASE?
				#print aa_first_letter
				
				lower = False #reset flag
				if(aa_first_letter.islower() == True):
					#print "converting to uppercase"
					aa_first_letter= aa_first_letter.upper()
					#print aa_first_letter
					numberlast = number
					number = re.sub("\D", "", aa)
					lower = True # a flag
				
				#get CO
				atom_shift = splitlist[indexpos]
				if(atom_shift == '-'):
					atom_shift = 0
				atom_shift = float(atom_shift)
				#print CO
				
				#use colist from shifts.py
				for dict in indexlist:
					if dict['aa'] == aa_first_letter:
						if lower == True:
							if(number != numberlast):
								i += 1
							#out = "?-" + number + " "
							out = "?~ "
							sys.stdout.write(out)
						else:
							i += 1
						#print "Shift", dict['shift'], "range:", dict['range']
						if((dict['shift'] + dict['range']) <= atom_shift):
							# -> 1
							print i, aa_first_letter, "CO", 1, "From (input, index):", atom_shift, dict['shift'], "Range:", dict['range']
							fileobj.write("%d %s %d %3.3f %3.3f\n" % (i, aa_first_letter, 1, atom_shift, dict['shift']))
						elif(atom_shift <= (dict['shift'] - dict['range'])):
							# -> -1
							fileobj.write("%d %s %d %3.3f %3.3f\n" % (i, aa_first_letter, -1, atom_shift, dict['shift']))
							print i, aa_first_letter, "CO", -1, "From (input, index):", atom_shift, dict['shift'], "Range:", dict['range']
						else:
							# -> 0
							fileobj.write("%d %s %d %3.3f %3.3f\n" % (i, aa_first_letter, 0, atom_shift, dict['shift']))
							print i, aa_first_letter, "CO", 0,  "From (input, index):", atom_shift, dict['shift'], "Range:", dict['range']
					
					
def make_files():
	#ARGS: index of 
	# 1 -> filename.txt
	# 2 -> index position of input
	# 3 -> indexlist
	compare_single_index("results/co.txt",2,colist)
	compare_single_index("results/ca.txt",3,calist)
	compare_single_index("results/cb.txt",4,cblist)
					
					
	
def main():
	print "Here you can enter a SINGLE space delimited sparky file of shifts. See example file for formatting questions\n"
	sparkyfile = read_input_file()
	read_a_line(sparkyfile)
	#debug:
	#print column_headings
	#print other_lines
	make_files()
	
	return 0




if __name__ == '__main__':
	main()
