from tkinter import *
import os
from shutil import move
import collections
import sys, getopt
from collections import Counter

def SearchDirectoryAndCopy(inputFolder,destFolder,extension):
	fileDICT={}
	result = {}
	number=0;
	if not os.path.exists(destFolder):
		os.makedirs(destFolder)
		
	for dirpath, dirnames, filenames in os.walk(inputFolder):
		for filename in [f for f in filenames if f.endswith(extension)]:
			#fileDICT[(os.path.join(dirpath, filename))] = [filename,dirpath]
			if not os.path.isfile(os.path.join(destFolder, filename)):
				move(os.path.join(dirpath, filename),destFolder)
			else:
				#rename and move
				fullpath = os.path.join(dirpath, filename)
				filename_split = os.path.splitext(fullpath)
				filename_zero, fileext = filename_split
				os.rename(fullpath, filename_zero + str(number)+fileext)
				move(os.path.join(fullpath,filename_zero + str(number)+fileext)	,destFolder)
				number+=1

				
	return
	

	
def main(argv):
   inputfile = ''
   outputfile = ''
   extension= ''
   try:
      opts, args = getopt.getopt(argv,"h:i:o:e:",["ifile=","ofile=","extension="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile> -e <extension>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile> -e <extension>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in("-e","--extension"):
         extension = arg
   print ('Input file is "', inputfile)
   print ('Output file is "', outputfile)
   print ('extension file is "', extension)
   SearchDirectoryAndCopy(inputfile,outputfile,extension)
   #dict = {'Name': [2,2], 'Age': 7, 'Class': 'First'}
   #print(dict)
   #os.rename("wynik","plik2.txt")

if __name__ == "__main__":
   main(sys.argv[1:])









