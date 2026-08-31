# Day 28 – Revision Day: Everything from Day 1 to Day 27

## What You've Covered So Far

| Days | Topic | Key Concepts |
|------|-------|-------------|
| 1 | DevOps & Cloud Intro | What is DevOps, SDLC, Cloud basics |
| 2–7 | Linux Fundamentals | Architecture, commands, processes, systemd, file system hierarchy, troubleshooting, text files |
| 8 | Cloud Server Setup | Docker, Nginx, web deployment |
| 9–11 | Users, Permissions & Ownership | User/group management, file permissions, chown/chgrp |
| 12 | Revision Day 1 | Days 1–11 recap |
| 13 | Volume Management | LVM — physical volumes, volume groups, logical volumes |
| 14–15 | Networking | Fundamentals, DNS, IP, subnets, ports, hands-on checks |
| 16–18 | Shell Scripting | Basics, loops, arguments, error handling, functions |
| 19–20 | Shell Scripting Projects | Log rotation, backup, crontab, log analyzer |
| 21 | Shell Scripting Cheat Sheet | Personal reference guide |
| 22–25 | Git & GitHub | Init, branching, merge, rebase, stash, cherry pick, reset, revert, branching strategies |
| 26 | GitHub CLI | Managing GitHub from the terminal |
| 27 | GitHub Profile | Profile README, repo organization, developer branding |

---

## Challenge Tasks

### Task 1: Self-Assessment Checklist
Go through the checklist below. For each item, mark yourself honestly:
- **Can do confidently**
- **Need to revisit**
- **Haven't done yet**

#### Linux
- [ Can do confidently ] Navigate the file system, create/move/delete files and directories
- [ Can do confidently ] Manage processes — list, kill, background/foreground
- [ Can do confidently ] Work with systemd — start, stop, enable, check status of services
- [ Can do confidently ] Read and edit text files using vi/vim or nano
- [ Can do confidently ] Troubleshoot CPU, memory, and disk issues using top, free, df, du
- [ Need to revisit ] Explain the Linux file system hierarchy (/, /etc, /var, /home, /tmp, etc.)
- [ Can do confidently ] Create users and groups, manage passwords
- [ Can do confidently ] Set file permissions using chmod (numeric and symbolic)
- [ Can do confidently ] Change file ownership with chown and chgrp
- [ Can do confidently ] Create and manage LVM volumes
- [ Need to revisit ] Check network connectivity — ping, curl, netstat, ss, dig, nslookup
- [ Need to revisit ] Explain DNS resolution, IP addressing, subnets, and common ports

#### Shell Scripting
- [ Can do confidently ] Write a script with variables, arguments, and user input
- [ Can do confidently ] Use if/elif/else and case statements
- [ Can do confidently ] Write for, while, and until loops
- [ Can do confidently ] Define and call functions with arguments and return values
- [Can do confidentl ] Use grep, awk, sed, sort, uniq for text processing
- [ Can do confidently ] Handle errors with set -e, set -u, set -o pipefail, trap
- [ Can do confidently ] Schedule scripts with crontab

#### Git & GitHub
- [ Can do confidently] Initialize a repo, stage, commit, and view history
- [Can do confidently ] Create and switch branches
- [Can do confidently ] Push to and pull from GitHub
- [Can do confidently ] Explain clone vs fork
- [Can do confidently ] Merge branches — understand fast-forward vs merge commit
- [Can do confidently ] Rebase a branch and explain when to use it vs merge
- [ Can do confidently] Use git stash and git stash pop
- [Can do confidently ] Cherry-pick a commit from another branch
- [Can do confidently ] Explain squash merge vs regular merge
- [Can do confidentlyCan do confidently ] Use git reset (soft, mixed, hard) and git revert
- [Can do confidently ] Explain GitFlow, GitHub Flow, and Trunk-Based Development
- [Can do confidently ] Use GitHub CLI to create repos, PRs, and issues

---

### Task 2: Revisit Your Weak Spots
1. Pick **3 topics** from the checklist where you marked "Need to revisit"
2. Go back to that day's challenge and redo the hands-on tasks
3. Document what you re-learned in `day-28-notes.md`

---

### Task 3: Quick-Fire Questions
Answer these from memory (no Googling). Then verify your answers:

1. What does `chmod 755 script.sh` do?
   - It will change file permission and will give rwx (read,write,execute)  access to the owner and rx (read,execute) access to the group and other user.

2. What is the difference between a process and a service?
     - Process : any running stance of the program
     - Service : a service is a background process 

3. How do you find which process is using port 8080?
   - Run to find process:  `netstat -tulnp |grep 8080`

4. What does `set -euo pipefail` do in a shell script?
   - its error handling command, it will exit the script as soon as it encounters any error.
   - set -e - exit if error occurs
   - set -u - exit if there is any undefine variable
   - set -o pipefail - exit if any pipe command fails

5. What is the difference between `git reset --hard` and `git revert`?
   - `git reset --hard` : head move back to given commit and changes will be deleted.
   - `git revert` : deleted the changes by adding a new commit.

6. What branching strategy would you recommend for a team of 5 developers shipping weekly?
   - GitHub flow

7. What does `git stash` do and when would you use it?
   - It temporarily save your changes so that you can work on some **hot fix** without loosing your work.
   - Use it when you are in need to switch the branch to do some **hot fix**. use `git stash` to save the current changes temporarily and switch the branch for hot fix.

8. How do you schedule a script to run every day at 3 AM?
   - Will use Cron job : 0 3 * * *

9. What is the difference between `git fetch` and `git pull`?
    - `git fetch` : it only download all the changes from remote repo.
    - `git pull` : download the changes and merge them with local

10. What is LVM and why would you use it instead of regular partitions?
    - LVM is a layer between physical disks and filesystems.
    - it is a flexible storage management system in Linux that lets you resize, combine, and manage disks dynamically, unlike regular partitions which are fixed in size once created.
      
---

### Task 4: Organize Your Work
1. Make sure all your daily submissions (day-1 through day-27) are committed and pushed [ ✅ ]
2. Check that your `git-commands.md` is up to date [ ✅ ]
3. Check that your shell scripting cheat sheet is complete [ ✅ ]
4. Verify your GitHub profile and repos are clean (from Day 27) [✅ ]

---

### Task 5: Teach It Back

- Explain Git branching to a non-developer
  Imaging you are writing an article and one of your fried want to contribute on that. You don't want him to work on the original file so that work remain intact.
  So you have created a copy of your original file and asked them to work on this file.
  The copy of your original file is actually a branch. You have the exact copy of original file and start working on it without affecting the original file.

---

