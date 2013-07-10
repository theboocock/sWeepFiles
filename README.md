Sweep Man Pigeon Data Outputter
===============================

Basically just takes in a raster file from some program I have never heard of
and outputs the two files are required there is plans for some customisation to
be added in later versions.

Usage
----
basically just run from your command environment in windows/mac/unix if
you have python installed.

#### Example Runs.

    Create the two output files from one input file
    - ``python sWeepMan.py -f <raster.txt>`` 
    
    Create the two output files for every file in a line seperated list
    - ``python sWeepMan.py -l <filelist.txt>`` 

    Change the total time after the first sweep occurs that the spikes are recorded to 50 seconds and read a single raster
    - ``python sWeepMan.py -l <filelist.txt> -t 50000``


Python Help
-----------


Usage: sWeepMan.py [options]

Options:
  -h, --help            show this help message and exit
  -f INPUT_FILE, --file=INPUT_FILE
                        Input File Type
  -l LIST_FILE, --file-list=LIST_FILE
                        Line seperated file containing file names of all the
                        files to create output
  -o OUTPUT_PREFIX, --prefix=OUTPUT_PREFIX
                        Output prefix the start of the output filenames
                        (should not be used if a file list is used
  -t READ_TIME, --total-time=READ_TIME
                        Total time spikes are recorded after the first sweep
                        occurs



