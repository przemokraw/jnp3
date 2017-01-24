FROM ubuntu:16.04
 
MAINTAINER mg359194

RUN apt-get update
RUN apt-get -y install nginx

COPY nginx.conf /etc/nginx/

EXPOSE 9999

CMD ["nginx"]
