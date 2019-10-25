# Supreme Bot 
## How to install 
1. install python 3.7
    - https://www.python.org/downloads/release/python-375/
2. (run): ```pip install pipenv```
3. (run):  ```pipenv install```


## How to install through Docker
## Structure and Explanation
##
## "-t" is the tag name you will be giving your image upon creation
## the "." at the end it IMPORTANT. It tells docker to look in the Current Directory for "Dockerfile"
1. docker build -t username/nickname-for-app .

## "-it" is needed for activation of interactive shell
## "--rm" tells docker to delete the container once you exit the contianer. Else, itll just be consuming space in the background
## "sh" at the end tells docker you want to use Shell to interact with the container
2. docker run -it --rm username/name-of-app sh



## Example
1. docker build -t brandonlv/dockerize-python-app .
2. docker run -it --rm brandonlv/dockerize-python-app sh
