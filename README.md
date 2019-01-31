# transactions_storage
Ethereum transactions storage for given address

## Requirements
* Python 3 (tested on 3.6)
* Celery
* Redis
* postgreSQL
* web3py

## How to use
1. Install Python3, requirements.txt.
2. Setup postgreSQL and Redis.
3. Create `tr_storage/local_settings`. Required fields:
    ```
    DATABASES = {
        'default': {
            'ENGINE':
            'NAME':
            'USER':
            'PASSWORD:
            'HOST': 
            'PORT': 
        }
    }
    
    BROKER_URL
    CELERY_RESULT_BACKEND
    
    INFURA_ENDPOINT
    
    ACCOUNT_ADDRESS
    ```

4. Add starting block for synchronizing:
    ```
    >>> from api.models import AppInfo
    >>> AppInfo.objects.create(last_polled_block_number=<Starting_block_number>)
    ```
5. Run celery beat and worker:
    ```
    $ celery beat -A tr_storage
    $ celery worker -A tr_storage
    ```
6. Run application:
    ```
    $ python manage.py runserver
    ```
## API Example

```
localhost:8000/api/transactions/
    ?fromAddress=0x03Db31B96CbB7ddEe5e887Ff71B6D22aa0a80b58&
    toAddress=0xC755525576d4e26819408ee604161cd20283d899&
    fromDate=1548898176&
    toDate=1548898542
```
Will return the following result:
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "hash": "0x68354901473afd2216a1a15c226025fb34315f304faf963f30b1ccf8de669886",
        "block_number": 4926043,
        "from_address": "0x03Db31B96CbB7ddEe5e887Ff71B6D22aa0A80B58",
        "to_address": "0xC755525576d4e26819408ee604161cd20283d899",
        "quantity": "10000000000000000",
        "timestamp": 1548898176,
        "input_data": "0x"
    },
    {
        "hash": "0x96f186b4c911acbb2b576fcedd9602981556e8b0b6c916ddbf1f62868803e550",
        "block_number": 4926066,
        "from_address": "0x03Db31B96CbB7ddEe5e887Ff71B6D22aa0A80B58",
        "to_address": "0xC755525576d4e26819408ee604161cd20283d899",
        "quantity": "300000000000000000",
        "timestamp": 1548898541,
        "input_data": "0x"
    }
]
```