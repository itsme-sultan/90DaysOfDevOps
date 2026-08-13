# Day 22 – Introduction to Git: Your First Repository


### Task 1: Install and Configure Git
1. Verify Git is installed on your machine
2. Set up your Git identity — name and email
3. Verify your configuration

![task1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-22/Images/task1.jpg)

---

### Task 2: Create Your Git Project
1. Create a new folder called `devops-git-practice`
2. Initialize it as a Git repository
3. Check the status — read and understand what Git is telling you
4. Explore the hidden `.git/` directory — look at what's inside

![task2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-22/Images/task2.jpg)

---

### Task 3: Create Your Git Commands Reference
1. Create a file called `git-commands.md` inside the repo
2. Add the Git commands you've used so far, organized by category:
   - **Setup & Config**
   - **Basic Workflow**
   - **Viewing Changes**
3. For each command, write:
   - What it does (1 line)
   - An example of how to use it

[git-commands.md](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-22/git-commands.md)

---

### Task 4: Stage and Commit
1. Stage your file
2. Check what's staged
3. Commit with a meaningful message
4. View your commit history

![task1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-22/Images/task4.jpg)

---

### Task 5: Make More Changes and Build History
1. Edit `git-commands.md` — add more commands as you discover them
2. Check what changed since your last commit
3. Stage and commit again with a different, descriptive message
4. Repeat this process at least **3 times** so you have multiple commits in your history
5. View the full history in a compact format

![task1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-22/Images/task5.jpg)

---

### Task 6: Understand the Git Workflow
1. What is the difference between `git add` and `git commit`?
   **Git add** :
   * Moves changes from your working directory into the staging area.
   * Files Marked "ready for the next snapshot."

   **Git commit** :
   * Takes everything currently in the staging area and permanently records it as a snapshot in your repository's history
      
3. What does the **staging area** do? Why doesn't Git just commit directly?
   * The staging area is like a shopping cart: you pick which changes you want to include in the next snapshot (commit).
   * If Git committed everything immediately, you’d lose flexibility. The staging area gives you control: Selective commits, Organized history.
     
5. What information does `git log` show you?
   * Git log give you complete commit history in a proper sequence. and allow you to know what changes has been made at what stage.
   * It includes the commit ID, author, date, and commit message for each change.
     
7. What is the `.git/` folder and what happens if you delete it?
   * The `.git/` folder is the heart of any Git repository. It’s a hidden directory that Git creates when you run `git init`.
   * Deleting `.git/` doesn’t delete your code, but it erases Git’s brain — the history and tracking system.
   * The folder becomes just a normal directory with no version control.
     
9. What is the difference between a **working directory**, **staging area**, and **repository**?
    * Working directory : This is your actual project folder in your system.
    * staging area :A middle ground between your edits and Git’s permanent history. You can pick and choose which changes to stage.
    * Repository :Where git stores all commits, branches, and history.

---
