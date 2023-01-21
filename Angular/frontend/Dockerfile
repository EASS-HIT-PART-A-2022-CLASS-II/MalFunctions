FROM node:16.13.0 as build
WORKDIR /app

RUN npm install -g @angular/cli

COPY ./package.json .
RUN npm install --save
COPY . .
RUN ng build

FROM nginx as runtime
COPY --from=build /app/dist/frontend /usr/share/nginx/html
