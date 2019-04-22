FROM redis
COPY redis.conf /usr/local/etc/redis/redis.conf
RUN sudo apt-get -y install nano
EXPOSE 6379
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]