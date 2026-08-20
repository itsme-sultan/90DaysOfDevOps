

**Setup & configuration**
```bash
1. git config --global user.name   #setup a user-name for all file & directory
2. git config --global user.email  #setup a user-email for all the file & directory
3. git config --list               #config info
```

**Basic workflow**
```bash
1. git init                         #Initialize a git repo
2. git add file-name                #stagged the changes
3. git commit -m "commit message"   #commit the changes
4. git commit -am "commit-message"  #stage & commit at the same time
5. git status                       #check untrack and stagged changes
6. git log                          #see all the commit history
7. git log --oneline                #commit history in oneline
8. git log --oneline origin/main    #commit history of remote branch
9. git log --oneline --graph        #Graph of branches and merges
10. git diff                        #changes of working-directory
```

**Git Branches**
```bash
1. git branch                   #list all the branches
2. git checkout feature         #switch to feature branch
3. git switch feature           #switch to feature branch
4. git branch feature           #create a new branch(feature)
5. git checkout -b feature      #create and switch to new branch
6. git branch -d feature        #delete feature branch
7. git branch -D                #forcefully delete branch
8. git branch -M dev            #rename current branch
```

**Remote command**
```bash
1. git remote -v                        #verify remote url
2. git remote add origin <link>         #setup remote url
3. git remote set-url origin <link>     #modify remote url
4. git clone <link>                     #clone git repo
5. git push origin main                 #push chnges on remote
6. git push -u origin main              #set upstream for remote
7. git fetch origin main                #download remote chnages
8. git fetch -p                         # git fetch & prune
```

**Merging & Rebasing**
```bash
1. git merge feature                    #merge current branch with feature
2. git rebase <branch>                  #move the branch commit on the tip of another branch
```

**Stash && Cherry-pick**
```bash
1. git stash                            #Hide the current work
2. git stash pop                        # bring back stash changes
3. git stash apply                      #bring back the stash changes and keep them in stash too
4. git stash list                       #see all the stash
5. git stash clear                      #delete all the stash
6. git stash drop stash@{0}              #delete specific stash
7. git cherry-pick <commit>             #merge specific commit
```

**undo Command**
```bash
1. git restore <file>                   #discard W.D changes
2. git restore --staged <file>          #unstage the chnages
3. git rm --cached <file>               #unstage & remove from git tracking
4. git reset --soft <commit_id>         #move the head to given commit, changes move to staging
5. git reset --mixed <commit_id>        #move head to given commit and unstage the changes
6. git reset --hard <coommit_id>        #move head to given commit and delete all the chnages from w.d
7. git reset Head~1                     #head moves back one commit, stagging area cleaned,W.d keep changes
8. git revert <commit>                  #undo the changes by creating new commit
```
 
