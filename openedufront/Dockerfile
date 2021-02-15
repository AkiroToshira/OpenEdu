FROM node:alpine3.10 AS builder

COPY . /app

WORKDIR /app

RUN yarn install && yarn build

FROM nginx:alpine
WORKDIR /usr/share/nginx/html
COPY --from=builder /app/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/build .
ENTRYPOINT ["nginx", "-g", "daemon off;"]