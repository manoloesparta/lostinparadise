# Lost in Paradise

> Funky music starts

Ths application serves as a way for CETYS university to manage their lost and found items that are found throughout the school year.

## Requirements
1. [Docker](https://www.docker.com/products/docker-desktop) 20+
2. docker compose 3+
3. make 4.1+
4. npm 6.14+
5. node 14.16+

## Usage

### Server
Make sure that Docker is running, open a terminal and on the server directory run
```bash
docker-compose build
```
After that on the same terminal run
```bash
docker-compose --env-file ./envs/dev.env up
```
### Client
Open a new terminal (without closing the last one), move to client directory, run
```bash
npm i
```
After that on the same terminal run
```bash
npm run start
```

## License
This project is under the MIT license
