## To add the customized_lib to the reachable libs:
```
import sys

sys.path.append('/Users/........./customizedlib')
```


## To go a better approach, add it to env vars:


```
vim ~/.bash_profile
```
then add the path to the env vars:
```
export PYTHONPATH='/Users/.../customizedlib')
```
## To install a pip library
```
python3 -m pip install <lib name>
```
