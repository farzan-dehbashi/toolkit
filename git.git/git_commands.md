### to view log files
```
git log
```
### To see short for of log files:
```
git log --oneline
```
### Git status
To see the status of what are commited and what are in staging area and what are local.
```
git status
```
To see one short:
```
git status -s
```
### See the changed lines of the files in the stagin area vs repository
```
git diff --staged
```
### See differences of working directory to staged
```
git diff
```
### Configure git
```
git config --system/--global/--local/ user.email <email>
git config <options> user.name
```
### To show what each commit has encompassed:
For the very last commit:
```
git show HEAD
```
For previous ones:
```
git show HEAD~<number of commits that you whant to go back>
```
### To see all of the files modified in a git commit:
```
git ls-tree HEAD
```
To view the file, you should use the identifier backed from the ls-tree command and feed it to:
```
git show <identifier e.g. 64629...>
```
### Objects 

#### Commits
#### Blogs (Files)
#### Trees (Directories)
#### Tags

### Restore
To undo add commands.
#### To restore a file from staging area and bring it back to working directory only:
```
 git restore --staged <file name>
```
#### To undo changes of a file
```
git restore <file name>
```
#### To undo git add:
```
git reset
```
##### Note that 'git restore' deletes all local changes to that file and 'git restore --staged', only removes the file from staging area and the local changes still remains intact.
## Branch
### Make a new branch
```
git branch <branch name>
```
### To view branches:
```
git branch
```
### To switch to the other branch
```
git checkout <branch name>
```
### To delete a branch
```
git branch -d <branch name>
```
## To revert changes
First step is to see what version do you want to get into. To do so, use <git log> then copy the hash of the commit and then use <git reset hash_number> to revert changes. But after this only the git file is heading toward that desired commit and not local files. To update local files use <git stash> to stash the local changes and then use git reset --hard to update the local files to match the head in the git file.
