import os
import sys
import math
from optparse import OptionParser

# Input parameters
#
# -f <Input_file>
# -l <List File>
# -o <output_prefix>
# List file is a line seperated file containing file names 
# to perform the datawrangling on and create the bins 
# as required.



# Bin_size is in ms 
# so 5000ms is 5 seconds
# 50 ms and 100 ms
def create_bins(bin_size,input_file,total_time):
    i = -1
    counts = [0] * int(math.floor(total_time/bin_size))
    count_list = []
    for line in input_file:
         #print(line)
         counts = [0] * int(math.floor(total_time/bin_size))
         if i == -1:
            i = i + 1
         else:
            line = line.split('\t')
            if(len(line) > 2):
                sweeps = line[2].strip().split(',')
                for sweep in sweeps:
                    msSweep = float(sweep) * 1000
                    #print(sweep)
                    msIndex = int(math.floor(msSweep/bin_size))
                    #print(msIndex)
                    counts[msIndex] = counts[msIndex] + 1
            count_list.append(counts)
    #print(count_list)
    return count_list 

def read_frequency_file(input_file,output_prefix=None,total_time=25000):
    if(output_prefix == None):
        output_prefix = input_file.split('.')[0]
    with open(input_file, 'r') as f:
        bin50ms = create_bins(50,f,total_time)
        f.seek(0) 
        bin100ms = create_bins(100,f,total_time)
        f.seek(0)
        bin5000ms = create_bins(5000,f,total_time)
    create_output_files(output_prefix,bin50ms,bin100ms,bin5000ms,total_time)

def create_output_files(output_prefix,bin50ms, bin100ms,bin5000ms,total_time=25000):
    versionOne = output_prefix + 'v1.txt'
    versionTwo = output_prefix + 'v2.txt'
    v2 =open(versionTwo,'w')
    v1 =open(versionOne,'w')
    fiftyLine = list(range(1,int(25000/50)+1))
    oneHundredLine = list(range(1,int(25000/100)+1))
    final_line = '\t' + '\t'.join([str(i) for i  in fiftyLine]) + '\t' +'\t'.join([str(i) for i in oneHundredLine])
    print(final_line)
    v1.write(final_line + '\n')
    # Read both lines into a string buffer
    for i in range(0,10):
       tempFiFty = bin50ms[i]
       tempOneHundred = bin100ms[i]
       final_line = str(i+1) +'\t' +'\t'.join([str(i) for i  in tempFiFty]) + '\t' +'\t'.join([str(i) for i in tempOneHundred])
       print(final_line)
       print(i)
       v1.write(final_line + '\n')
   
    v1.close()
    for i in range(0,len(bin5000ms[0])):
        final_line = str(i+1) + '\t'
        for j in range(0,len(bin5000ms)):
            print(final_line + str(bin5000ms[j][i]) )
           
            v2.write(final_line + str(bin5000ms[j][i]) + '\n' )
    
    # create oneway anova output tables     
    v2.close()
def read_list(list_file,output_prefix=None,total_time=25000):
    with(open(list_file,'r')) as f:
        for line in f:
            read_frequency_file(line,total_time=total_time)

def main():
    parser =OptionParser()
    parser.add_option('-f','--file', dest="input_file", help="Input File Type")
    parser.add_option('-l','--file-list',dest="list_file",help="Line seperated file containing file names of all the files to create output")
    parser.add_option('-o', '--prefix', dest="output_prefix",help="Output prefix the start of the output filenames (should not be used if a file list is used")
    parser.add_option('-t', '--total-time',dest="read_time",help="Total time spikes are recorded after the first sweep occurs")
    (options , args) = parser.parse_args()
    if(options.input_file):
        read_frequency_file(options.input_file,options.output_prefix)
    elif(options.list_file):
        read_list(options.file_list,options.output_prefix)
    

if __name__=="__main__":main()
