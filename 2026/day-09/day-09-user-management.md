# Day 09 – Linux User & Group Management

## Task 1: Create Users  
- Created three new user with home directory ` tokyo, berlin & professor `  
  Command : ` sudo adduser <name> `  
  Verify : Verified new user ` cat /etc/passwd ` and checked home directory `ls -ltr /home`.

![newuser](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-09/newuser.jpg)

----

## Task 2: Create Groups
- Created two group devlopers & admins  
  Commands : ` sudo groupadd devloprs/admins `  
  Verify : Confirm the new group using command ` cat /etc/group `

  ---
  
## Task 3: Assign to Groups 

- Assign user to group : tokyo → developers
  ` sudo usermod -aG devlopers tokyo `
  
- Assign user to group : berlin → developers + admins (both groups)  
  ` sudo usermod -aG devlopers berlin `  
  ` sudo usermod -aG admins berlin `
  
  - Assign user to group : professor → admins  
    `sudo usermod -aG admins professor `

Verify : Check if user is added to the group  
- Command : ` cat /etc/group `

![groupassign](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-09/add-group.jpg)

---

## Task 4: Shared Directory 
- Create directory: /opt/dev-project  
  ` mkdir /opt/dev-project `
  
- Set group owner to developers  
  ` sudo chgrp devlopers /opt/dev-project `
  
- Set permissions to 775 (rwxrwxr-x)  
  ` sudo chmod 775 /opt/dev-project `
  
- Test by creating files as tokyo and berlin  
  
Verify: Check permissions and test file creation  
` ls -ltr /opt/dev-project `

![shared-directory](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-09/Task4.jpg)

----

## Task 5: Team Workspace
- Create user nairobi with home directory  
  ` sudo adduser nairobi `
  
- Create group project-team  
  ` sudo groupadd project-team `
  
- Add nairobi and tokyo to project-team  
  ` sudo usermod -aG project-team nairobi `  
  ` sudo usermod -aG project-team tokyo `
  
- Create /opt/team-workspace directory  
  ` sudo mkdir /opt/team-worksapce `
  
- Set group to project-team, permissions to 775  
  `sudo chmod 775 /opt/team-worksapce `
  
- Test by creating file as nairobi

![task5](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-09/Task5.jpg)

    
