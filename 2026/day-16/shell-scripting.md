# Day 16 – Shell Scripting Basics

## Task 1: Your First Script  
1. Create a file `hello.sh`
2. Add the shebang line `#!/bin/bash` at the top
3. Print `Hello, DevOps!` using `echo`
4. Make it executable and run it

```bash
chmod +x hello.sh
./hello.sh
```

**Document:** What happens if you remove the shebang line?
- I remove the shabang from the screip and run it directly `./hello.sh` and cript executed successfully.  
  Since bash is the default interpreter. I checked it using command `$0`

  ![task1]()

  ------------

## Task 2: Variables  
1. Create `variables.sh` with:
   - A variable for your `NAME`
   - A variable for your `ROLE` (e.g., "DevOps Engineer")
   - Print: `Hello, I am <NAME> and I am a <ROLE>`
2. Try using single quotes vs double quotes — what's the difference?
 * Using double quote `" "` - The variables and commands are evaluated.
 * Using single quote `' '` - Single quotes preserve the string literally — no word splitting, no expansion.
   
   Note : Since value of name & role are ('SUltan Ansari' & 'Devops engineer' ) just simple text with no special characters, single quotes are perfectly safe.  
   Where it does become an issue:
   1. If the value contains a single quote — e.g.: NAME='O'Brien'
   2. If the value itself needs expansion — e.g. you wanted to embed another variable inside:  NAME='Mr. $LASTNAME'
  
  ----------

## Task 3: User Input with read
1. Create `greet.sh` that:
   - Asks the user for their name using `read`
   - Asks for their favourite tool
   - Prints: `Hello <name>, your favourite tool is <tool>`

     ![greet.sh]()

----------


## Task 4: If-Else Conditions
1. Create `check_number.sh` that:
   - Takes a number using `read`
   - Prints whether it is **positive**, **negative**, or **zero**

     ![check-number.sh]()

2. Create `file_check.sh` that:
   - Asks for a filename
   - Checks if the file **exists** using `-f`
   - Prints appropriate message
   - 
     ![file-check]()

  ----------- 
  
## Task 5: Combine It All  
Create `server_check.sh` that:
1. Stores a service name in a variable (e.g., `nginx`, `sshd`)
2. Asks the user: "Do you want to check the status? (y/n)"
3. If `y` — runs `systemctl status <service>` and prints whether it's **active** or **not**
4. If `n` — prints "Skipped."

   ![server-check]()
  
