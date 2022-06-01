# Endpoints List

These are the API endpoints the client will be communicating to.

## Users

- POST /login

  Request

  ```json
  {
    "body": {
      "username": "t030046",
      "password": "ultrasecurepassword"
    }
  }
  ```

  Response

  > Login Successfully

  ```json
  {
    "status": 200,
    "data": {
      "x-jwt-key": "blah.blah.blah"
    }
  }
  ```

  > Not matched credentials

  ```json
  {
    "status": 400,
    "error": "No match for username or password"
  }
  ```

## Status

- GET /health

  Request

  ```json
  {}
  ```

  Response

  > Server is up

  ```json
  {
    "status": 200,
    "message": "hello there"
  }
  ```

## Auth

- POST /validate

  Request

  ```json
  {
    "headers": {
      "x-jwt-key": "blah.blah.blah"
    }
  }
  ```

  Response

  > Valid

  ```json
  {
    "status": 200,
    "message": "user is registered"
  }
  ```

  > Invalid

  ```json
  {
    "status": 400,
    "error": "username not valid"
  }
  ```

## Search

- POST /search

  Request

  ```json
  {
    "headers": {
      "x-jwt-key": "blah.blah.blah"
    },
    "body": {
      "query": "laptop gris"
    }
  }
  ```

  Response

  > Matching results

  ```json
  {
    "status": 200,
    "data": {
      "items": [
        {
          "id": "uuid",
          "status": "Entregado",
          "category": "Electronico",
          "description": "Cargador Dell Punta chica Azul Salón 7307,",
          "found": "2020-01-24"
        },
        {
          "id": "uuid",
          "status": "Entregado",
          "category": "Electronico",
          "description": "Audífonos BITS, Salón 2201, ",
          "date": "2019-09-05"
        },
        {
          "id": "uuid",
          "status": "Entregado",
          "category": "Electronico",
          "description": "Cargador HP 1303",
          "date": "2019-11-07"
        },
        {
          "id": "uuid",
          "status": "Entregado",
          "category": "Electronico",
          "description": "Cargador Genérico Punta Grande Salón 1306,",
          "date": "2019-09-23"
        },
        {
          "id": "uuid",
          "status": "Entregado",
          "category": "Electronico",
          "description": "Cargador LAPTOP GENERICO 1306",
          "date": "2019-11-07"
        }
      ]
    }
  }
  ```
