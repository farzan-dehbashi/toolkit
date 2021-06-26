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

