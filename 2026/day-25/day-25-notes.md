# Day 25 – Git Reset vs Revert & Branching Strategies

### Task 1: Git Reset — Hands-On
1. Make 3 commits in your practice repo (commit A, B, C)
2. Use `git reset --soft` to go back one commit — what happens to the changes?

![Task.1 -2]()

3. Re-commit, then use `git reset --mixed` to go back one commit — what happens now?

![Taskk.1 -3]()

4. Re-commit, then use `git reset --hard` to go back one commit — what happens this time?

![Task.1 -4]()

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
     * `--reset` : when you want to completely remove commits and all changes.

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

![Task.2]()

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

| | `git reset` | `git revert` |
|---|---|---|
| What it does | undo the changes & move the branch pointer | undo the changes by adding new commit |
| Removes commit from history? | Yes | No |
| Safe for shared/pushed branches? | No  | Yes |
| When to use | cleaning up local, unpushed commits | commit has already been pushed |

---

### Task 4: Branching Strategies
Research the following branching strategies and document each in your notes with:
- How it works (short description)
- A simple diagram or flow (text-based is fine)
- When/where it's used
- Pros and cons

1. **GitFlow** — develop, feature, release, hotfix branches
2. **GitHub Flow** — simple, single main branch + feature branches
3. **Trunk-Based Development** — everyone commits to main, short-lived branches
4. Answer:
   - Which strategy would you use for a startup shipping fast?
   - Which strategy would you use for a large team with scheduled releases?
   - Which one does your favorite open-source project use? (check any repo on GitHub)

---

### Task 5: Git Commands Reference Update
Update your `git-commands.md` to cover everything from Days 22–25:
- Setup & Config
- Basic Workflow (add, commit, status, log, diff)
- Branching (branch, checkout, switch)
- Remote (push, pull, fetch, clone, fork)
- Merging & Rebasing
- Stash & Cherry Pick
- Reset & Revert

---

**TrainWithShubham**
