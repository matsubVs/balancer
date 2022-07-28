FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d
COPY default2.conf /etc/nginx/conf.d
COPY status_server.conf /etc/nginx/conf.d
COPY balancer.conf /etc/nginx/conf.d