# Day 26 – GitHub CLI: Manage GitHub from Your Terminal

### Task 1: Install and Authenticate
1. Install the GitHub CLI on your machine
2. Authenticate with your GitHub account
3. Verify you're logged in and check which account is active

![Task.1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-26/Images/Task.1.jpg)

4. Answer in your notes: What authentication methods does `gh` support?
   * Browser-based OAuth
   * Personal Access Token (PAT)
   * SSH Key-based

---

### Task 2: Working with Repositories
1. Create a **new GitHub repo** directly from the terminal — make it public with a README

![Task.2-1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-26/Images/Task.2-1.png)

2. Clone a repo using `gh` instead of `git clone`

![Task.2-2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-26/Images/Task.2-2.jpg)

3. View details of one of your repos from the terminal

![Task.2-3](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-26/Images/Task.2-3.jpg)

4. List all your repositories

![Task.2-4](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-26/Images/Task.2-4.jpg)

5. Open a repo in your browser directly from the terminal
6. Delete the test repo you created (be careful!)

![task.2-6](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-26/Images/task.2-6.jpg)


---

### Task 3: Issues
1. Create an issue on one of your repos from the terminal — give it a title, body, and a label

![Task.3-1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-26/Images/Task.3-1.png)

2. List all open issues on that repo
![Task.3-2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-26/Images/Task.3-2.jpg)

3. View a specific issue by its number
![Task.3-3](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-26/Images/Task.3-3.jpg)

4. Close an issue from the terminal
![Task.3-4](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-26/Images/Task.3-4.jpg)

5. Answer in your notes: How could you use `gh issue` in a script or automation?
   - By combining gh issue commands in a script,you can automatically:
        - Check open issues
        - Add comments
        - Close issues

    - Example:
        ```bash
        gh issue list --repo srdangat/gh-cli-task-day26
        gh issue comment 1 --repo srdangat/gh-cli-task-day26 --body "Checked automatically."
        gh issue close 1 --repo srdangat/gh-cli-task-day26
        ```

---

### Task 4: Pull Requests
1. Create a branch, make a change, push it, and create a **pull request** entirely from the terminal
![Task.4.1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-26/Images/Task.4-1.png)

2. List all open PRs on a repo
3. View the details of your PR — check its status, reviewers, and checks
4. Merge your PR from the terminal
![task.4-2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-26/Images/Task.4-2.jpg)

5. Answer in your notes:
   - What merge methods does `gh pr merge` support?
     * `gh pr merge` supports `merge commit`, `squash merge` , and `rebase merge`.
       
   - How would you review someone else's PR using `gh`?
     * `gh pr review <PR-number>`

---

### Task 5: GitHub Actions & Workflows (Preview)
1. List the workflow runs on any public repo that uses GitHub Actions
2. View the status of a specific workflow run
![Task.5-1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-26/Images/Task.5-1.png)

3. Answer in your notes: How could `gh run` and `gh workflow` be useful in a CI/CD pipeline?
   - In a CI/CD pipeline, the `gh run` and `gh workflow` commands are powerful because they let you interact directly with GitHub Actions from the command line.
   - perfect for automation, scripting, or debugging. 

---

