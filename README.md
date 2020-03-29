# Basic DRF project

## Run


```
\\ clone and then in build folder
docker build . -t basedjango:2
\\ clone project into "mydrf" volume and then:
sudo docker run --rm -it -p 8000:8000 -v mydrf:/usr/src/app/mydjangoapp basedjango:2
```


