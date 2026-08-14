# Day 23 – Git Branching & Working with GitHub

### Task 1: Understanding Branches
1. What is a branch in Git?
   - A branch is like a separate timeline of your project.
   - Think of it as a copy of the code where you can work on new features.
     
3. Why do we use branches instead of committing everything to `main`?
   - You can test features or fixes without breaking the main code.
   - Different people can work on different branches at the same time.
     
5. What is `HEAD` in Git?
   - `HEAD` is a special pointer that tells you where you currently are in your project’s history.
   - It always points to the latest commit on the branch you are working on.
     
7. What happens to your files when you switch branches?
   - Git updates your working directory and replaced with the versions from the branch you switched to.

---

### Task 2: Branching Commands — Hands-On
In your `devops-git-practice` repo, perform the following:
1. List all branches in your repo
   ```bash
   git branch
   ```
3. Create a new branch called `feature-1`
   ```bash
   git branch feature-1
   ```
5. Switch to `feature-1`
   ```bash
   git checkout feature-1
   ```
7. Create a new branch and switch to it in a single command — call it `feaRestore files to a previous committure-2`.
   ```bash
   git checkout -b feature-2
   ```
![delete](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-23/Images/task2-delete.jpg)

9. Try using `git switch` to move between branches — how is it different from `git checkout`?
    
    - git switch :Newer, simpler command. Designed only for branch operations.
    - git checkout :Older, multi‑purpose command. Can do several things:
      * Switch branches - `git checkout <branch>`
      * Restore files to a previous commit - `git checkout HEAD~1 file.txt `
        
11. Make a commit on `feature-1` that does **not** exist on `main`
12. Switch back to `main` — verify that the commit from `feature-1` is not there
13. Delete a branch you no longer need
    ```bash
    git branch -d feature-2
    ```
    
15. Add all branching commands to your `git-commands.md`

![task2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-23/Images/task2.jpg)

---

### Task 3: Push to GitHub
1. Create a **new repository** on GitHub (do NOT initialize it with a README)
2. Connect your local `devops-git-practice` repo to the GitHub remote
3. Push your `main` branch to GitHub
4. Push `feature-1` branch to GitHub

![task-3](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-23/Images/Task-3.png)

6. Verify both branches are visible on GitHub

![Github](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-23/Images/task-3-github.jpg)

8. Answer in your notes: What is the difference between `origin` and `upstream`?
   - Origin : Default name for the remote repository you cloned from
     * Example : git clone https://github.com/itsme-sultan/devops-git-practice.git
     * Git automatically names that remote origin. your personal copy of the repo (your fork or clone).
       
   - Upstream : The original repo you forked from is added manually as upstream
     * upstream = the source repo you forked from (the “parent project”).
     * Example : https://github.com/TrainWithShubham/90DaysOfDevOps.git
     * This lets you pull updates from the original project:
       ```bash
       git fetch upstream
       git merge upstream/master
       ```
---

### Task 4: Pull from GitHub
1. Make a change to a file **directly on GitHub** (use the GitHub editor)

![task4](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-23/Images/Task-4.jpg)

3. Pull that change to your local repo

![task4.2]()

5. Answer in your notes: What is the difference between `git fetch` and `git pull`?
   - `git fetch` : Downloads changes from remote only; does not change your branch,just updates remote info.
   - `git pull` : Downloads changes from remote and merges them into your current branch, updating your local branch immediately.

---

### Task 5: Clone vs Fork
1. **Clone** any public repository from GitHub to your local machine

![task5.1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-23/Images/Task5.1.jpg)

3. **Fork** the same repository on GitHub, then clone your fork

![task5.2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-23/Images/task5.2.jpg)

5. Answer in your notes:
   - What is the difference between clone and fork?
     
     * Clone : Clone is a Git command that copies a repository from a remote location (like GitHub) to your local machine.
     * Fork :  Fork is a GitHub/GitLab/Bitbucket platform feature (not a Git command). It creates your own copy of someone else's repository on the platform, under your account
       
   - When would you clone vs fork?
     When Clone:
     - You have write access to the repo (e.g., it's your own project or you're on the team).
     - You just need a local working copy — no intention of contributing back independently.
     - Example: cloning your company's private repo you're already a collaborator on.

      When Fork:
      - You don't have write access to the original repo (common with open source projects).
      - You want to make changes and eventually propose them back via a pull request, without affecting the original.
      - You want to experiment freely on your own copy without risk to the upstream project.
      - Example: contributing a bug fix to a popular open-source library — fork it, clone your fork, make changes, push to your fork, then open a PR to the original.
        
   - After forking, how do you keep your fork in sync with the original repo?
     * After forking and cloning my fork, I add the original repository as an upstream remote. Then I fetch changes from upstream, merge the upstream default branch into my current branch, and push the updates to my fork.
       ```bash
       git remote add upstream git@github.com:aws-containers/retail-store-sample-app.git  #Add the original repo as a remote
       git checkout main                     #checkout to main branch
       git fetch upstream                    #Fetch the latest changes from upstream
       git merge upstream/main               #Merge upstream changes into your local main
       git push origin main                  #Push the updated main branch to your fork on GitHub

       Note: Use rebase instead of merge if you prefer a linear history
       ```

---
