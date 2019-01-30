FROM node:latest

WORKDIR /client
ADD ./package.json ./package.json
ADD ./package-lock.json ./package-lock.json

RUN npm install

ADD . .

CMD ["npm", "run", "serve"]
