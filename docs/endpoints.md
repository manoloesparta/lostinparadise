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
        "statusCode": 200,
        "message": {
            "X-Jwt-Token": "blah.blah.blah"
        }
    }
    ```

    > Not matched credentials

    ```json
    {
        "statusCode": 400,
        "message": "Incorrect username or password"
    }
    ```

    * POST /logout

    Request

    ```json
    {
        "header": {
            "X-Jwt-Token": "blah.blah.blah"
        }
    }
    ```

    Response

    > Token invalidated

    ```json
    {
        "status": 200,
        "message": "logout succesfully"
    }
    ```

## Search

* POST /search

    Request

    ```json
    {
        "headers": {
            "X-Jwt-Token": "blah.blah.blah"
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
        "statusCode": 200,
        "message": {
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
