# File Ownership Challenge (chown & chgrp)

## Task 1: Understanding Ownership

- Run ls -l in your home directory
- Identify the owner and group columns
- Check who owns your files
- Format: -rw-r--r-- 1 owner group size date filename

  ![TAsk1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-11/Task1.jpg)


**Owner** : The owner is usually the user who created the file or directory. Owner can change permission of file.  
**Goup** : The group is a collection of users who have similar access to the file or directory.

---

## Task 2: Basic chown Operations  

- Create file devops-file.txt
- Check current owner: ls -l devops-file.txt
- Change owner to tokyo (create user if needed)
- Change owner to berlin
- Verify the changes

  ![Task2]( https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-11/Task2.jpg)

  -----

## Task 3: Basic chgrp Operations 

- Create file team-notes.txt
- Check current group: ls -l team-notes.txt
- Create group: sudo groupadd heist-team
- Change file group to heist-team
- Verify the change

  ![Task3](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-11/Task3.jpg )

  ----

## Task 4: Combined Owner & Group Change  
Using `chown` you can change both owner and group together:

- Create file project-config.yaml
- Change owner to professor AND group to heist-team (one command)
- Create directory app-logs/
- Change its owner to berlin and group to heist-team

  ![Task4](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-11/Task4.jpg )

  ----
## Task 5: Recursive Ownership 

1. Create directory structure:
   ```bash
   mkdir -p heist-project/vault
   mkdir -p heist-project/plans
   touch heist-project/vault/gold.txt
   touch heist-project/plans/strategy.conf
   ```

2. Create group `planners`: `sudo groupadd planners`

3. Change ownership of entire `heist-project/` directory:
   - Owner: `professor`
   - Group: `planners`
   - Use recursive flag (`-R`)

4. Verify all files and subdirectories changed: `ls -lR heist-project/`

   ![Task5](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-11/Task5.jpg)

   ----
   
## Task 6: Practice Challenge

1. Create users: `tokyo`, `berlin`, `nairobi` (if not already created)
2. Create groups: `vault-team`, `tech-team`
3. Create directory: `bank-heist/`
4. Create 3 files inside:
   ```
   touch bank-heist/access-codes.txt
   touch bank-heist/blueprints.pdf
   touch bank-heist/escape-plan.txt
   ```

5. Set different ownership:
   
   - `access-codes.txt` → owner: `tokyo`, group: `vault-team`  
   - `blueprints.pdf` → owner: `berlin`, group: `tech-team`  
   - `escape-plan.txt` → owner: `nairobi`, group: `vault-team`  

   ![Task6](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-11/Task6.jpg)
