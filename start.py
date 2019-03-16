import os
import time 
import sys
from multiprocessing import Process
import signal
import subprocess
from threading import *
from contextlib import redirect_stdout
import io

#MAIN FUNCTION 
def main():
	selectedProblem=''
	problem_path=''

	# PROBLEMS IS A DICTIONARY WHICH CONTAIN ALL THE PROBLEMS
	Problems = {'1' : 'problem_1' ,'2' : 'problem_2', '3':'problem_number'}

	# PROBLEM_FILE IS A DICTIONARY WHICH CONTAINS THE INPUT FILE PATH
	Problem_file = {'problem_1' : '/home/sj1328/Desktop/some_file_1.txt', 'problem_2' : './a.txt', 'problem_no' : 'problem_path'}
	print('Select Your Problem which you want to submit : ')
	
	# PRINTS THE LIST OF PROBLEMS
	for keys,values in Problems.items():
		print(keys,values)

	# TAKE INPUT
	selectedProblem = input()
	try:
		# CONTAINS PATH OF INPUT FILE
		problem_path = Problem_file[Problems[selectedProblem]]
		file = open(problem_path)
		file.close()
	except:
		print('\n\n------Invalid Option Selected : ------\n\n')
		#IF PATH IS INVALID THEN THE JUDGE WILL TERMINATE
		sys.exit()


	#CONTAINS LANGUAGE	
	Language = {'1' : 'C', '2' : 'C++', '3' : 'Python 2', '4' : 'Python 3.6', '5' : 'Ruby'}
	print('Select Your Language')

	#PRINT THE LIST OF LANGUAGE
	for keys,values in Language.items():
		print (keys,values)
	Language_option = int(input())


	#COMPARE FUNCTION COMPARES THE OUTPUT FILE WITH THE CORRECT OUTPUT
	def compare():
		flag = 0
		line_no = 0
		#FILE1 IS THE CORRECT OUTPUT FILE
		file1 = open('./a.txt')
		#FILE2 IS THE OUTPUT FILE BY THE SUBMITTED CODE
		file2 = open('run'+str(selectedProblem)+'.txt')
		f1_line = file1.readline()
		f2_line = file2.readline()
		while f1_line!='' or f2_line!='':
			f1_line = f1_line.rstrip()
			f2_line = f2_line.rstrip()
			if f1_line != f2_line:
				flag = 1
				break;
			line_no +=1
			f1_line = file1.readline()
			f2_line = file2.readline()
		if flag==0:
			f1_line = file1.readline()
			f2_line = file2.readline()
			f1_line = f1_line.rstrip()
			f2_line = f2_line.rstrip()
			if f1_line != f2_line:
				print('Wrong Answer')
			else:
				print('Accepted')
		else:
			print('Wrong Answer')


	#JUDGE FUNCTION WORKS AS A JUDGE
	def judge():
		# LANGUAGE SELECTION IN WHICH THE CODE IS SUBMITTED
		if(Language_option==1):
			# OPENS A FILE IN WHICH THE OUTPUT OF CODE IS WRITTEN
			file2 = open('run'+str(selectedProblem)+'.txt','w+')

			#PATH OF THE CODE
			print('Give the path of the code : ')
			path = input('')
			try:
				#MAKES THE OBJECT FILE
				os.system('gcc ' + path + ' -o run'+str(selectedProblem))

				#COMMAND WHICH RUNS THE OBJECT FILE
				cmd = './run'+str(selectedProblem) +' < input'+selectedProblem+'.txt'
				handle = ''

				#FUNCTION FOR THE THREAD
				def thread_1(handle):
					handle = os.popen(cmd).read() 

				# THREAD OBJECT
				th_1 = Process(target= thread_1, args = (handle,))
				# STARTING THE THREAD
				th_1.start()
				th_1.join(1.5) 	

				#CHECKING WHETHER THE THREAD IS FINISHED OR NOT
				if th_1.is_alive():
					#IF THREAD IN ALIVE THEN TERMINATE THE PROCESS
					th_1.terminate()
					print('Tle')
				else:
					handle = os.popen(cmd).read()
					#WRITING THE OUTPUT IN THE FILE 
					file2.write(handle)
					file2.close()
					#COMPARE THE OUTPUT
					compare()
			
			except :
				print('Error')

			# DELETING THE OUTPUT FILE CREATED
			os.system('rm -rf run'+selectedProblem)
			os.system('rm -rf run'+selectedProblem+'.txt')
		elif(Language_option==2):
			#FILE CREATED TO SAVE THE OUTPUT
			file2 = open('run'+str(selectedProblem)+'.txt','w+')

			#PATH OF THE CODE
			print('Give the path of the code : ')
			path = input('')
			try:
				#OBJECT FILE
				os.system('g++ ' + path + ' -o run'+str(selectedProblem))
				handle = ''

				#THREAD FUNCTION
				def thread_1(handle):
					handle = os.popen('./run'+str(selectedProblem)+' < input'+selectedProblem+'.txt').read()

				# THREAD OBJECT 
				th_1 = Process(target= thread_1, args = (handle,))
				
				#THREAD STARTED
				th_1.start()
				th_1.join(1.5) 

				#THREAD IS ALIVE OR NOT	
				if th_1.is_alive():
					th_1.terminate()
					print('Tle')
				else:
					handle = os.popen('./run'+str(selectedProblem)+' < input'+selectedProblem+'.txt').read()
					#WRITNG THE OUTPUT IN THE FILE
					file2.write(handle)
					file2.close()
					compare()

			except:
				print('Error')

			# DELETING THE FILES CREATED
			os.system('rm -rf run'+selectedProblem)
			os.system('rm -rf run'+selectedProblem+'.txt')
		elif(Language_option==3):
			# FILE CREATED FOR OUTPUT FILE 
			file2 = open('run'+str(selectedProblem)+'.txt','w+')

			#PATH OF THE CODE
			print('Give the path of the code : ')
			path = input('')
			try:
				handle = ''
				#THREAD FUNCTION
				def thread_1(handle):
					handle = os.popen('python '+path+' < input'+selectedProblem+'.txt' ).read()

				#THREAD OBJECT
				th_1 = Process(target= thread_1, args = (handle,))
				
				#STARTING THREAD 
				th_1.start()
				th_1.join(1.5)

				#THREAD IS ALIVE OR NOT
				if th_1.is_alive():
					th_1.terminate()
					print('Tle')
				else:
					handle = os.popen('python '+path+' < input'+selectedProblem+'.txt').read()
					file2.write(line)
					file2.close()
					compare()
			except:
				print('Error')

			os.system('rm -rf run'+selectedProblem+'.txt')
		elif(Language_option==4):
			file2 = open('run'+str(selectedProblem)+'.txt','w+')
			print('Give the path of the code : ')
			path = input('')
			try:
				handle = ''
				def thread_1(handle):
					handle = os.popen('python3 '+path+' < input'+selectedProblem+'.txt').read()

				th_1 = Process(target= thread_1, args = (handle,))
				th_1.start()
				th_1.join(1.5)

				if th_1.is_alive():
					th_1.terminate()
					print('Tle')
				else:
					handle = os.popen('python3 '+path+' < input'+selectedProblem+'.txt').read()
					file2.write(line)
					file2.close()
					compare()
			except:
				print('Error')

			os.system('rm -rf run'+selectedProblem+'.txt')
		elif(Language_option==5):
			file2 = open('run'+str(selectedProblem)+'.txt','w+')
			print('Give the path of the code : ')
			path = input('')
			try:
				handle = ''
				def thread_1(handle):
					handle = os.popen('ruby '+path+' < input'+selectedProblem+'.txt').read()
				
				th_1 = Process(target= thread_1, args = (handle,))
				th_1.start()
				th_1.join(1.5)

				if th_1.is_alive():
					th_1.terminate()
					print('Tle')
				else:
					handle = os.popen('ruby '+path+' < input'+selectedProblem+'.txt').read()
					file2.write(line)
					file2.close()
					compare()
			except:
				print('Error')

			os.system('rm -rf run'+selectedProblem+'.txt')
		else:
			# IF WRONG LANGUAGE SELECTION
			print('Wrong Input : ')
			Language_selection()
			judge()

	# CALLING JUDGE FUNCTION
	judge()


while(True):
	#LOOP FOR JUDGE
	main()

	#WHETHER WANTS JUDGE TO CONTINUE OR NOT
	print('Do You Want To Continue (y/n) : ')
	continue_judge=input()
	if(continue_judge=='n'):
		break;
