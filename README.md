# Lost in Paradise

> Funky music starts

Ths application serves as a way for CETYS university to manage their lost and found items that are found throughout the school year.

## Requirements
- Docker 20.10+
- docker compose 3.0+
- make 4.1+
- npm 6.14+
- node 14.16+

## Usage

### Server
You must be on server directory before running these commands!

The following command is for starting the server
```bash
make dev
```
The following commands is for loading data to server
```bash
make load
```
The following command is for deleting the data from the server
```bash
make wipe
```
**If you cant start the server, try deleting and loading all data again.**
### Client
You must be on client directory before running these commands!

This command will install all the applications dependencies
```bash
npm i
```
This will start the application
```bash
npm run start
```

## License
This project is under the MIT license
