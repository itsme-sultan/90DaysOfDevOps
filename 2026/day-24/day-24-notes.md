# Day 24 – Advanced Git: Merge, Rebase, Stash & Cherry Pick


### Task 1: Git Merge — Hands-On
1. Create a new branch `feature-login` from `main`, add a couple of commits to it
2. Switch back to `main` and merge `feature-login` into `main`
3. Observe the merge — did Git do a **fast-forward** merge or a **merge commit**?
   - Observation : merge the feature-login branch with main and observe that it was **fast-forward** merge.

![git-merge](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/git-merge.jpg)

5. Now create another branch `feature-signup`, add commits to it — but also add a commit to `main` before merging
6. Merge `feature-signup` into `main` — what happens this time?
   - Observation : This time merge was not the fast-forward, a new merge commit was added unlike fast-forward.

![merge-signup](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/git-signup-merge.jpg)

8. Answer in your notes:
   - What is a fast-forward merge?
     * When you merge a diverge branch into main branch and there is no new commit in the main branch since branch is diverged then merge is known as fast-forward.
     * No new merge commit is created.
    
       ```bash
       main :  A - B -C
                       |       
       feature:        D - E - F
       ff-merge : A - B -C -D -E -F
       ```
   - When does Git create a merge commit instead?
     * Git creates a merge commit when the two branches you’re trying to combine have diverged histories.
     * meaning both branches have new commits since they split.
    
       ```bash
       main:    A — B — E — F
       feature: A — B — C — D
       #both main & feature have commit after b.
       ```

   - What is a merge conflict? (try creating one intentionally by editing the same line in both branches)
     * A merge conflict happens in Git when two branches have modified the same part of a file differently
     * and Git cannot automatically decide which change to keep.

![git-conflict](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/git-conflict.jpg)
    
---

### Task 2: Git Rebase — Hands-On
1. Create a branch `feature-dashboard` from `main`, add 2-3 commit

![Task.2-1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/Task.2-1.jpg)

2. While on `main`, add a new commit (so `main` moves ahead)

![task.2-2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/task.2-2.jpg)

3. Switch to `feature-dashboard` and rebase it onto `main`

![task.2-rebase](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/Task.2-rebase.jpg)

4. Observe your `git log --oneline --graph --all` — how does the history look compared to a merge?

![task.2-log](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/task.2-log.jpg)

5. Answer in your notes:
   - What does rebase actually do to your commits?
     * Rebase rewrite the commit history of current branch, move current branch commits to the tip of another brnach.
     * Move the commit history of feature-dashboard on the tip of main branch one by one.
       
   - How is the history different from a merge?
     * `merge` preserves history exactly as it happened. creates a merge commit.
     * `rebase` rewrites history. moves your commits on top of feature-dashboard branch,creates a linear,clean history.no merge commit.
       
   - Why should you **never rebase commits that have been pushed and shared** with others?
     * Rebasing rewrites commit history — it creates brand new commits with different SHA hashes. This causes real problems once others have pulled the original commits.
       
   - When would you use rebase vs merge?
     * Use rebase when you are working on your local branch and want a linear, clean history.
     * Use merge when you are working on shared branch and want to preserve the commit history.

---

### Task 3: Squash Commit vs Merge Commit
1. Create a branch `feature-profile`, add 4-5 small commits (typo fix, formatting, etc.)

![Task.3-1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/Task.3-1.jpg)

2. Merge it into `main` using `--squash` — what happens?

![task.3-squash](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/Task.3-squash-merge.jpg)

3. Check `git log` — how many commits were added to `main`?

![Task.3-log](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/Task.3-log.png)

4. Now create another branch `feature-settings`, add a few commits
5. Merge it into `main` **without** `--squash` (regular merge) — compare the history

![task.3-merge](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/task3.merge.png)

6. Answer in your notes:
   - What does squash merging do?
     * Combines all commits from a feature branch into one single commit on main.
     * Does not preserve individual commit history.
       
   - When would you use squash merge vs regular merge?
     * squash merge: Feature branch has many commits.You want clean main branch history.
     * regular merge: You want to preserve full commit history.
       
   - What is the trade-off of squashing?
     * The trade-off of squashing is that while it keeps the main branch history clean and linear,it removes the detailed commit history of the feature branch by combining everything into a single commit.

---

### Task 4: Git Stash — Hands-On
1. Start making changes to a file but **do not commit**
2. Now imagine you need to urgently switch to another branch — try switching. What happens?
   * `If there is no conflict` :Git will let the checkout/switch happen, and your uncommitted changes carry over with you to the new branch. They stay in your        working directory as uncommitted modifications.
   * `Conflict` : Git blocks the switch entirely. You can't proceed until you either commit, stash, or discard the changes.

![task.4-2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/Task.4-2.png)

3. Use `git stash` to save your work-in-progress
4. Switch to another branch, do some work, switch back
5. Apply your stashed changes using `git stash pop`
6. Try stashing multiple times and list all stashes
7. Try applying a specific stash from the list

![Task.4-6](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/Task.4-6.png)

8. Answer in your notes:
   - What is the difference between `git stash pop` and `git stash apply`?
     * `git stash pop` bring back the changes & remove them from the stash.
     *  `git stash apply` bring back the stash changes but keep them in stash too.
      
   - When would you use stash in a real-world workflow?
     * If I’m working on a feature and need to urgently switch branches to fix a production bug,I would use git stash to temporarily save my unfinished changes        before switching.

---

### Task 5: Cherry Picking
1. Create a branch `feature-hotfix`, make 3 commits with different changes

![Task.5-1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/Task.5-1.jpg)

2. Switch to `main`
3. Cherry-pick **only the second commit** from `feature-hotfix` onto `main`

![task.5-3](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/Task.5-3.jpg)

4. Verify with `git log` that only that one commit was applied

![tassk.5-4](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-24/Images/Task.5-4.jpg)

5. Answer in your notes:
   - What does cherry-pick do?
     * Cherry-pick merge a given commit changes only without merging whole feature branch.
       
   - When would you use cherry-pick in a real project?
     * You fixed a bug on feature branch, but you need that fix on main too without merging whole feature branch.
       
   - What can go wrong with cherry-picking?
     * merge conflicts if same file was modified.
     * Commit history confusion because it creates new commit ids.

---


