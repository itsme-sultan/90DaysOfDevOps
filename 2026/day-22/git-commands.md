

**Setup & configuration**
1. git config --global user.name   #setup a user-name for all file & directory
2. git config --global user.email  #setup a user-email for all the file & directory
3. git config --list               #config info


**Basic workflow**
1. git init                         #Initialize a git repo
2. git add file-name                #stagged the changes
3. git commit -m "commit message"   #commit the changes
4. git commit -a -m "commit-message"    #stage & commit at the same time

**Viewing chnages**
1. git status           #check untrack and stagged changes
2. git log              #see all the commit history
3. git log --oneline    #commit history in oneline
4. git log --oneline origin/main    #commit history of remote branch
5. git diff             #changes of working-directory

**Git Branches**
1. git branch                   #list all the branches
2. git checkout feature         #switch to feature branch
3. git switch feature           #switch to feature branch
4. git branch feature           #create a new branch(feature)
5. git checkout -b feature      #create and switch to new branch
6. git branch -d feature        #delete feature branch
7. git branch -D                #forcefully delete branch
8. git branch -M dev            #rename current branch

**Remote command**
1. git remote -v                        #verify remote url
2. git remote add origin <link>         #setup remote url
3. git remote set-url origin <link>     #modify remote url
4. git clone <link>                     #clone git repo
5. git push origin main                 #push chnges on remote
6. git push -u origin main              #set upstream for remote
7. git merge feature                    #merge with current branch with feature branch
