FROM ubuntu:16.04
 
MAINTAINER mg359194

RUN apt-get update
RUN apt-get -y install nginx

RUN mkdir /data
RUN mkdir /data/www
RUN mkdir /data/images

COPY nginx.conf /etc/nginx/
COPY index.html /data/www/
COPY ./images /data/images/

EXPOSE 80

CMD ["nginx"]
