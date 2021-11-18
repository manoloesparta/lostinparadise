# Lost in Paradise

> Funky music starts

Ths application serves as a way for CETYS university to manage their lost and found items that are found throughout the school year.

## Requirements
1. Docker 20.10+
2. docker compose 3.0+
3. make 4.1+
4. npm 6.14+
5. node 14.16+

## Usage

### Server
You must be on server directory before running these commands!

Make sure that Docker is running, open a terminal and run
```bash
docker-compose --env-file ./envs/dev.env up
```
This will start the server

To load data run
```bash
docker-compose up -d mongo 
```
and
```bash
$(PYTHON) scripts/load_data.py
```

To wipe data run
```bash
docker-compose down
```
and
```bash
sudo rm -rf database
```
### Client
You must be on client directory before running these commands!

Open a new terminal (without closing the last one) and run
```bash
npm i
```
After that on the same terminal run
```bash
npm run start
```

## License
This project is under the MIT license
