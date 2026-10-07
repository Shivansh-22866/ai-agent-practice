 docker run -p 9201:80 \
        -e PGADMIN_DEFAULT_EMAIL="user@domain.com" \
        -e PGADMIN_DEFAULT_PASSWORD="secret" \
        dpage/pgadmin4