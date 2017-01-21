#This script will rename all files in a directory to be the same lenth by appending "0"s to the beginning for easy sorting.

import os

files = []
files.append([])
files.append([])
filePath = 'Enter Path Containing Files Here' #Note: this should just contain files to be renamed, no folders

response = raw_input("Dry run (D) or Real Rename (R)?")


for (path, dirnames, filenames) in os.walk(filePath): 
    files[0].extend(os.path.join(path, name) for name in filenames) #Capture full path
    files[1].extend(filenames) #Capture just filename

length = 0; #This will store the file name length

#print files[1]
for num in range(0,len(files[1])):
	currentLenth = len(files[1][num]) #For each file, determine the lenght of the filename
	if currentLenth > length:
		length = currentLenth #Update largest length with current file's lenght if it's the longest found so far
 
print "The longest file is ", length, " characters long"

for num in range(0,len(files[1])): #Loop through all filenames in the directory
	oldString = files[1][num]
	currentString = oldString
	while (len(currentString) < length): 
		currentString = "0" + currentString #Append "0"s to the beginning of the filename until the length matches the longest file name
	if response == "R": #If rename is chosen, do the renaming
		os.rename(filePath + '\\' + oldString, filePath + '\\' + currentString)
		print oldString + " ---> " + currentString + " Renamed!"
	elif response == "D": #If it's a dry run, just print the intended rename
		print oldString + " ---> " + currentString + " Dry run"

