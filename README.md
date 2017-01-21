# FileNameEqualizer
This script will rename files in a directory such that all of their file names are the same length. Useful for numeric sorting.

# Use Case

For example, let's say you have a directory containing the following images:

* 1.jpg
* 2.jpg
* 4.jpg
* 6.jpg
* 11.jpg
* 12.jpg
* 13.jpg
* 22.jpg

If you sort these by name, you normally get:

* 1.jpg
* 11.jpg
* 12.jpg
* 13.jpg
* 2.jpg
* 22.jpg
* 4.jpg
* 6.jpg

The solution is to rename the files such that they are the same length. Such as:

* 01.jpg
* 02.jpg
* 04.jpg
* 06.jpg
* 11.jpg
* 12.jpg
* 13.jpg
* 22.jpg

This sorts by name just as desired. And this is what this script does for you!

# How to Use

1. Open the script in your favorite text editor.
2. Put your directory path under filePath, replacing 'Enter Path Containing Files Here' with your path.
2. Run the python script, and choose "dry run" (option D) to print out the intended rename without actually performing it.
3. The script will output each filename in the following format: "oldFileName ---> newFileName Dry Run".
4. If you are satisfied with how the files will be renamed, re-run the script, but choose to rename (option R).
5. File names will be appended with "0"s to match the longest file name.
6. You can now sort numerically with ease!

