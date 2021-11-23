##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: Nov 22
## Modified: Nov 22 2021
## Email: farzan.dehbashi95@gmail.com
## Status: Stack implementaition
##################################################

# Implementing stack by dequeue

from collections import deque

stack = deque()

stack.append('hi')
print(stack)
print(stack.pop())
print(stack)