FROM docker.elastic.co/beats/filebeat:7.0.0
USER root
# RUN chown root:filebeat /usr/share/filebeat/filebeat.yml
# RUN rm /usr/share/filebeat/filebeat.yml
COPY filebeat.yml /etc/filebeat/filebeat.yml
COPY log_files /app/log_files
# CMD ["filebeat", "-e", "-strict.perms=false"]
RUN chmod go-w /etc/filebeat/filebeat.yml
USER filebeat
# RUN chown -R root /usr/share/filebeat/
# RUN chmod -R go-w /usr/share/filebeat/
CMD ["filebeat", "-e", "-c", "/etc/filebeat/filebeat.yml"]
