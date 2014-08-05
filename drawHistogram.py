###############################################
#
#    drawHistogram.py
#
#    Copyright (C) 2014 Evan Denmark
#
#        
#    Creates a histogram of the lengths of reads within a FASTA file
#    This is free software with the intent of making bioinformatics research more easy and efficient.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################

import numpy
import pylab
import argparse

parser = argparse.ArgumentParser(description = 'Please provide your FASTA file and (optionally) the number of bins you would like in your histogram (default is 10)')
parser.add_argument('fasta',help= 'a FASTA file of your data')
parser.add_argument('-num_bins',default = 10, type=int, help= 'the number of bins in your histogram')

your_file = parser.parse_args().fasta
num_bins = parser.parse_args().num_bins

new_file = open(your_file, 'r')

total = []
n=0
for each_line in new_file:
	each_line.rstrip('\n').lstrip('\n')
	if each_line[0] == '>':
		total.append(n)		
		n=0
		
	else:
		for each_char in each_line:
						
			n+=1

avg = (float(sum(total))/(len(total)))
print 'Average: ', avg

ylist = []
for name in name_list:
	ylist.append(len_dict[name])

pylab.hist(total,num_bins, (0,max(total)))
pylab.title('Length of Reads')
pylab.xlabel('Length of Nucleotide Sequence')
pylab.ylabel('Number of Sequences')
pylab.show()

