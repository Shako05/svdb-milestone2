FROM alpine:latest
RUN apk add --no-cache lighttpd
COPY index.html /var/www/localhost/htdocs/
EXPOSE 80
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]