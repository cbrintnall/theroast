FROM node:9.6.1

COPY . /app
WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install
RUN npm install react-scripts@1.1.1 -g

CMD ["npm", "start"]