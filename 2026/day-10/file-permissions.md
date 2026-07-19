# Day 10 – File Permissions & File Operations 

## Task 1: Create Files 
- Create empty file devops.txt using touch
- Create notes.txt with some content using echo
- Create script.sh using vim with content: echo "Hello DevOps"

  ![Task1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-10/Task1.jpg)

-----

## Task 2: Read Files
- Read notes.txt using cat
- View script.sh in vim read-only mode
- Display first 5 lines of /etc/passwd using head
- Display last 5 lines of /etc/passwd using tail

  ![Task2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-10/Task2.1.jpg)
  ![Task2.1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-10/Task2.jpg)

-------------

## Task 3: Understand Permissions 
- Format: rwxrwxrwx (owner-group-others)

- r = read (4), w = write (2), x = execute (1)
- Check your files: ls -l devops.txt notes.txt script.sh

- Answer: What are current permissions? Who can read/write/execute?

  ![file-permission]()
  
  File devops.txt & notes.txt have samme file permission.

  ```bash
  - → regular file (not a directory)
  Owner (Ubuntu): rw- → read ✅ write ✅ execute ❌
  Group (Ubuntu): rw- → read ✅ write ✅ execute ❌
  Others        : r-- → read ✅ write ❌ execute ❌
  ```

  File script .sh

  ```bash
  - → regular file (not a directory)
  Owner (Ubuntu): rw- → read ✅ write ✅ execute ✅
  Group (Ununtu): rw- → read ✅ write ✅ execute ✅
  Others        : r-- → read ✅ write ❌ execute ✅
  ```

  ![Task3](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-10/Task3.jpg)
  
----

## Task 4: Modify Permissions
- Make script.sh executable → run it with ./script.sh
- Set devops.txt to read-only (remove write for all)
- Set notes.txt to 640 (owner: rw, group: r, others: none)


  ![Task4](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-10/Task4.jpg)

----

## Task 5: Test Permissions
- Try writing to a read-only file - what happens?
- Try executing a file without execute permission
- Document the error messages

  ![Task5](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-10/task5.jpg)




