docker container ls
docker container stop <id>
docker container run --publish 80:80 --detach nginx # --publish open ops a port for the container
or:
```
docker container run -d -p 3306:3306 --name dbb -e MYSQL_RANDOM_ROOT_PASSWORD=yes mysql #e is environment variable
```
docker container logs <container name>
docker container rm -f <id> # to remove a container by force
### Run a mysql server
```
docker container run -d -p 3306:3306 --name dbb -e MYSQL_RANDOM_ROOT_PASSWORD=yes mysql #e is environment variable
docker container logs <container name> # to get the password
docker container run -d --name webserver -p 8080:80 httpd
docker container run -d --name proxy -p 80:80 nginx
```
### To see whats going on inside a container
```
docker container top <container name>
```
Shows the process inside. Exactly like top command works in linux.
```
docker container inspect <container name>
```
the above shows a json of inactive stuff of a container.
To get real time data like activity monitor:
```
docker container stats
```
### To get a shell into a container is:
```
docker container run -i -t --name <container name> <container type> bash#-t is a sudo tty simillar to ssh and -i keeps the thing open to be able to run more stuff
```
#### To get a shell into container by starting, use -ai instead of -it

# Images

## To get a specific image version:
```
docker pull <image_name>:<version>
``` 
For example:
```
docker pull nginx:1.11.9
```
