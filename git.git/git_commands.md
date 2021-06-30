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
### See the changed lines of the files in the stagin area 
```
git diff --staged
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
##### Note that 'git restore' deletes all local changes to that file and 'git restore --staged', only removes the file from staging area and the local changes still remains intact.
