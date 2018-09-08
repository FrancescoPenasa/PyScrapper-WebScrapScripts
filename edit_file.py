import os, sys

fname = input("Name of the folder where to copy the files (folder must not exist): ")

from_path = os.getcwd()		#actual path
to_path = os.path.join(from_path, fname) 	#where to create folder
os.makedirs(to_path)			#create folder

for filename in os.listdir(from_path):		#trova tutt i file nella cartella
	if (filename != fname):
		f(to_path,filename)
	else:
		pass


def f(to_path,filename):


	keyword_start = '<div id="news-stream">'
	keyword_stop  = '<div id="listamessaggi">'
	enter_var = False
	exit_var = False

	from_file = open(filename, 'r')

	lines = []
	for line in from_file.readlines():
		if (keyword_start in line):
			enter_var = True		
		elif (keyword_stop in line):
			exit_var = True
		if (enter_var and (not exit_var)):
			lines.append(line)

	from_file.close()


	to_file = open(str(os.path.join(to_path, filename))+'txt', 'w')

	to_file.writelines(lines)

	to_file.close()



