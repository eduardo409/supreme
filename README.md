# Supreme Bot
## How to install through Docker
### Example
1. ```docker build -t brandonlv/dockerize-python-app .```
2. ```docker run -it --rm brandonlv/dockerize-python-app sh```


### Structure Template and Explanation

> ```docker build -t username/nickname-for-app .```
> ```docker run -it --rm username/nickname-of-app sh```

1. "-t" is the tag name you will be giving your image upon creation
* the "." at the end it IMPORTANT. It tells docker to look in the current directory for "Dockerfile"
* "-it" is needed for activation of interactive shell
* "--rm" tells docker to delete the container once you exit the contianer. Else, itll just be consuming space in th$
* "sh" at the end tells docker you want to use Shell to interact with the container



### HELPFUL Docker Commands 

1. docker ps        # list of current running containers
2. docker ps -a     # list of all containers that have NOT been deleted.
2. docker images    # list of all images built. You can always reference these
