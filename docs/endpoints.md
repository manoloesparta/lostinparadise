# Endpoints List

These are the API endpoints the client will be communicating to.

## Users

* POST /login

    Request

    ```json
    {
        "body": {
            "username": "t030046",
            "password": "o"
        }
    }
    ```

    Response

    > Login Successfully

    ```json
    {
        "status": 200,
        "data": {
            "X-Jwt-Key": "blah.blah.blah"
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

## Auth

* POST /validate

    Request

    ```json
    {
        "headers": {
            "X-Jwt-Key": "blah.blah.blah",
        }
    }
    ```

    Response

    > Valid
    ```json
    {
        "status": 200
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

* POST /search

    Request

    ```json
    {
        "headers": {
            "x-jwt-key": "blah.blah.blah"
        },
        "body": {
            "start": "0",
            "keywords": "laptop gris"
        }
    }
    ```

    Response

    > Matching results

    ```json
    {
        "status": 200,
        "data": {
            "count": "16",
            "items": [
                {
                    "icon": "laptop",
                    "name": "HP Laptop",
                    "description": "Color gris con sticker de flor",
                    "date": "12/3/2020"
                },
                {
                    "icon": "laptop",
                    "name": "Lenovo Laptop",
                    "description": "Color entre negro y gris con sticker de flor",
                    "date": "5/11/2020"
                },
                {
                    "icon": "laptop",
                    "name": "macbook pro 2012",
                    "description": "macbook pro viejita",
                    "date": "22/6/2020"
                },
            ]
        }
    }
    ```
