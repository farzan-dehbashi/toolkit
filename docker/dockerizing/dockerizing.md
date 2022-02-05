# Dockerizing a simple python file
Link: https://www.youtube.com/watch?v=8uaDoMuDK6E&t=841s&ab_channel=DigitalSreeni
It is easy! You should generate a Docker file. In order to make docker get to know what files of your container should be used and what other additional images should be used to make your container work. 
make a <Dockerfile>
```
touch Dockerfile
``` 
Then, edit it:
```
FROM python:3
```
Means fetch python3 image from docker hub and put it in my intended directory so that my docker container can use it from now on. Then, copy your files:
These include your python files and/or any other code you have written. You should copy it to your container so that the stand alone container can use these codes.
```
COPY <file_name.py>
```
Then install some libraries needed. Like numpy, ...
```
RUN pip3 install <numpy>
```
Then run your <main.py> code:
```
CMD ["python3", "<main.py>"]
```
Above line is a cmd command which transtlates to <python3 main.py>. You may run any other command like this.

### Additional commands
```
WORKDIR <directory>
```
You may ignore this. WORKDIR is like cd in linux. To change the directory if needed.
