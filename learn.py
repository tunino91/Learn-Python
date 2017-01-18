import numpy as np 
import os
from os import path
import shutil
from os import listdir
from os.path import isfile, join
########	GLOBALLY DEFINED VARIABLES	  ########	
var_1 = 0 
var_2 = 0
var_3 = 0
##################################################
print 'var_1 is globally defined as: ', var_1

class firstClass():

	def function_1(self):
		var_1 = 'var_1'
		print 'var_1\'s value inside firstClass\'s funtion_1 is: ',var_1


	def function_2(self):
		var_2 = 'var_2'
		print var_2

class secondClass(firstClass):

	def function_3(self):
		var_3 = 'var_3'
		print var_3

	def function_1(self): #inhereted function from first class has been overwritten
		var_1 = 'Pastengo'
		print 'var_1\'s value is overwritten inside the second class from \'var_1\' to :', var_1


def main():

	var_1 = 'tuna'
	print 'The value of var_1 inside main() is: ',var_1

	########	CLASS OBJECTS ARE DEFINED	  ########

	obj_first_class = firstClass() 	
	obj_second_class = secondClass()
	##################################################

	########	ACCESSING FUNCTIONS INSIDE THE CORRESPONDING CLASSES	 ########

	obj_first_class.function_1()	# Execute the function_1
	obj_second_class.function_1() 	# Execute the overwritten function, funtion_1
	#############################################################################


	########	WORKING WITH FILES	  ########
	print '########	WORKING WITH FILES	  ########'

	f = open('nameOfTheFile.txt','w+')	# open() has two args: 
										# 1) Name of the file
										# 2) w: write, r: read, a: appending, +: if file doesn't exist,create one for me
	for i in range(1,10):

		f.write('This is the %d th line \r' %i ) # \r: new line for MacOS

	f.close()

	f = open('nameOfTheFile.txt','a+')  
	for i in range(10,20):
		f.write('This is the %d th line \r' %i )

	f.close()

	f = open('nameOfTheFile.txt','r')

	if f.mode == 'r': 		# check to make sure that file was open!
		contents = f.read() # reads the whole file at once, not good for reading big files
		print 'Printing the content of the written file:\r ',contents
		f.close()

	######## BEST WAY TO READ A BIG FILE ########
	with open('nameOfTheFile.txt','r') as f:	# 'with': handles opening and closing of the file
		txt = f.readlines()						# txt is equal to one line at a time
		for line in txt:
			print line
	


	print 'OS Name is: ', os.name
	print 'Does the Item in this path exist?: ', path.exists('nameOfTheFile.txt')
	print 'This \'Item\' is a file?: ', path.isfile('nameOfTheFile.txt') 
	print 'This \'Item\' is a directory?: ', path.isdir('nameOfTheFile.txt')
	 



	# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	if path.exists('nameOfTheFile.txt'):
		src = path.realpath('nameOfTheFile.txt')# Item's full path 
		x,y=path.split(src) 					# Splits the path of the file from it's name
		print 'Item\'s full path is: ',src 
		print 'Using path.split func, name of the file is extracted: ',y # Split func returns 2 values, x:path,y:name

		dst = src + '.bak'	# Added .bak at the end of the path(i.e path/nameOfTheFile.txt.bak)  
		shutil.copy(src,dst) # Made a bakcup file 

		os.rename('nameOfTheFile.txt','newFileName.txt') # nameOfTheFile.txt is changed to newFileName

if __name__ == '__main__':
	main()





print 'Outside of the main(), var_1 is back to being it\'s globally defined version: ',var_1 




