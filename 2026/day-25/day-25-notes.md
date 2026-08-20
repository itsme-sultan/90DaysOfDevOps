# Day 25 – Git Reset vs Revert & Branching Strategies

### Task 1: Git Reset — Hands-On
1. Make 3 commits in your practice repo (commit A, B, C)
2. Use `git reset --soft` to go back one commit — what happens to the changes?

![Task.1 -2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-25/Images/Task.1%20-2.png)

3. Re-commit, then use `git reset --mixed` to go back one commit — what happens now?

![Taskk.1 -3](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-25/Images/Task.1%20-3.png)

4. Re-commit, then use `git reset --hard` to go back one commit — what happens this time?

![Task.1 -4](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-25/Images/Task.1%20-4.png)

5. Answer in your notes:
   - What is the difference between `--soft`, `--mixed`, and `--hard`?
     * ` --soft ` - Move head  back to given commit, Changes move to staging area.
     * ` --mixed ` - Move head  back to given commit, unstage the changes
     * `--hard` - Move head  back to given commit, discard all the changes from working directory.
       
   - Which one is destructive and why?
     * `--hard` is destructive because it permanently discards all uncommitted changes in your staging area and working directory.
       
   - When would you use each one?
     * `--soft`  : when you want to undo a commit but keep changes staged,for example to edit the commit message.
     * `--mixed` : when you want to undo a commit and unstage changes,so you can modify them before recommitting.
     * `--hard` : when you want to completely remove commits and all changes.

   - Should you ever use `git reset` on commits that are already pushed?
     * No, once commits are pushed, others may have already pulled and worked on them, so resetting them can cause confusion and conflicts.

---

### Task 2: Git Revert — Hands-On
1. Make 3 commits (commit X, Y, Z)
2. Revert commit Y (the middle one) — what happens?
   * It causes conflict as revert remove the changes made by the `Commit -Y`.
   * `Commit -Z` made on top of Y trying to touch same line added and changed by the `commit-Y`.
     
3. Check `git log` — is commit Y still in the history?
   * `commit -Y` is still part of the history. revert just undo the changes by adding a new revert commit but keep the given commit.

![Task.2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-25/Images/Task.2.png)

4. Answer in your notes:
   - How is `git revert` different from `git reset`?
     * `git revert` : Creates a new commit that undo the changes from a previous commit. Keeps original commit in history.
     * `git reset` : Can rewrite history. Moves the branch pointer to an earlier commit.
       
   - Why is revert considered **safer** than reset for shared branches?
     * `revert` never rewrites commits that already exist — it only adds a new one.
     * `reset` rewrites the branch's history by literally moving the pointer backward.
       
   - When would you use revert vs reset?
     * `git revert` when : The commit has already been pushed and others may have pulled it (shared branch like main/master).
     * `git reset` when : You're cleaning up local, unpushed commits

---

### Task 3: Reset vs Revert — Summary
Create a comparison in your notes:

|       |    `git reset`    |    `git revert`    |
|---|:---:|:---:|
| What it does | undo the changes & move the branch pointer | undo the changes by adding new commit |
| Removes commit from history? | Yes | No |
| Safe for shared/pushed branches? | No  | Yes |
| When to use | cleaning up local, unpushed commits | commit has already been pushed |

---

### Task 4: Branching Strategies

1. **GitFlow** — develop, feature, release, hotfix branches
   - How it works:
     GitFlow uses a strict set of long-lived and short-lived branches with defined roles:

      * `main` — always reflects production-ready code
      * `develop` — integration branch for ongoing work
      * `feature` — branched from develop, merged back into develop
      * `release` — branched from develop when preparing a release; merged into both main and develop
      * `hotfix` — branched from main to patch production urgently; merged into both main and develop

   - Diagram :
     ```bash
   
           main  o---------------------o---------o---------o
                 \                   / \       /
      release     \        o--------o   \     /  (hotfix)
                   \       /              \   \
      develop       o-----o------o---------o---o
                     \     \      \
      feature          o----o      o-- (feature/x)
                       (feature/y)
      ```

   - When/where it's used :
     * Projects with scheduled releases (versioned software, desktop apps, embedded systems)
     * Teams that need to support multiple production versions simultaneously
    
   - Pros:
     * Clear separation of concerns (in-progress work vs. release-ready vs. production)
     * Good for managing multiple release versions in parallel

   - Cons :
     * Heavyweight: many long-lived branches increase merge complexity and conflicts
     * Slows down continuous delivery — not ideal for frequent deploys
       

2. **GitHub Flow** - simple, single main branch + feature branches
   - How it works:
     A lightweight model with a single long-lived branch, main, which is always deployable:
     
     * Create a `feature` branch off `main`
     * Commit work, push, open a pull request
     * Discuss/review, run CI
     * Merge into main
     * Deploy immediately (often automatically)

   - Diagram :

     ```bash
     main o---------o-------------o-----o
           \        ^  \          ^
            \        merge         merge
             o--o--o /       o--o-o
             feature/login    feature/signup
     ```

   - When/where it's used
     * Teams practicing CI/CD with frequent, small releases
     * GitHub's own workflow model (hence the name); common in open-source projects
    
   - Pros:
     * Simple and easy to understand — minimal branch types
     * Fast feedback loop; pairs naturally with CI/CD pipelines
    
   - Cons:
     * No dedicated structure for managing multiple release versions at once

3. **Trunk-Based Development** — everyone commits to main, short-lived branches
   - How it works :
     * All developers commit directly (or via very short-lived branches, often <1 day) to a single shared branch — the "trunk" `(main/trunk)` .

   - Diagram :

     ```bash
      [main] (The Trunk)
      |
      o (Start)
      |
      |\_ _ _ _ _ _ _ 
      |             \
      |              o (Dev A: Small Change)
      |<_ _ _ _ _ _ /
      |             /
      o (Merge & Test)
      |
      |\_ _ _ _ _ _ _ 
      |             \
      |              o (Dev B: Small Change)
      |<_ _ _ _ _ _ /
      |             /
      o (Merge & Test)
      |
      v
     ```

   - When/where it's used :
     * High-velocity engineering orgs practicing CI/CD (e.g., Google, Meta, Netflix-style setups)

   - Pros :
     * Minimizes merge conflicts — integration happens constantly, in small pieces

   - Cons :
     * Requires mature CI, automated testing, and feature-flag discipline — risky without it

   
4. Answer:
   - Which strategy would you use for a startup shipping fast?
     * GitHub Flow or Trunk-Based Development
   - Which strategy would you use for a large team with scheduled releases?
     * Gitflow
       
   - Which one does your favorite open-source project use? (check any repo on GitHub)  
     https://github.com/aws-containers/retail-store-sample-app (GithubFlow)

---

### Task 5: Git Commands Reference Update
https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-25/git-commands.md
