## Linux Fundamentals: Read and Write Text Files

1. created new empty file.  
   `touch notes.txt`

2. Added a new line using redirection operator.  
   `echo "Line 1" > notes.txt`

3. used `tee` command to add new line as well print the output.  
   `echo "Line 3" | tee -a notes.txt`

4. used `cat` command to print the content of the file.  
   `cat notes.txt`

5. printed first two line of the file.  
   `head -n 2 notes.txt`

6. Printed last two line of the file.  
   `tail -n 2 notes.txt`

![notes](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-06/notes.txt.jpg)
