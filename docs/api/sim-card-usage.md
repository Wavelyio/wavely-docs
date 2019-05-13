# Sim Card Usage
Usage for individual sim cards can be accessed using the usage api. 
We partition usage into 4 categories, **data**, **sms**, **smpp**, and **calls**. 
Each of these usage types have their own endpoint requiring that requests specify the **month** and **year** for which to retrieve the usage. 

Parameters for **years** must be given in the ISO **year** format such as 2019.
Months must be specified using the english names for months, such as january, march, and july.

When querying it is also required to specify which sim card the usage should be retrieved for.
This is done using the **icc** identifier of a sim card.

## Data usage for a sim card
Data usage for a given **month** in a given **year** can be accesed by using the following URL:

`GET /simcards/{icc}/usage/data/{year}/{month}`

**Response structure and type**
| Field       | Type     | Description                                                             |
| ----------- | -------- | ----------------------------------------------------------------------- |
| icc         | String   | The unique identifier for the sim card generating the usage.            |
| year        | Number   | Year is given in the ISO format for example 2019.                       |
| month       | Number   | Month is represented as a number for example 'april = 4'                |
| usageDate   | ISO 8601 |                                                                         |
| bytesIn     | Number   |                                                                         |
| bytesOut    | Number   |                                                                         |
| sessionId   | String   | Unique identifier for the session on the network.                       |
| imei        | String   | The observed Imei number for the device generating the usage.           |
| countryCode | String   | Alpha2 code                                                             |

**Example response**
```json
[
    {
        "icc": "89454284200010500094",
        "year": 2019,
        "month": 5,
        "usageDate": "2019-05-13T09:09:41+00:00",
        "bytesIn": 5687,
        "bytesOut": 2345,
        "sessionId": "5a095ef3-pgw-c/64e1a109",
        "imei": "3573100500176526",
        "countryCode": "DK"
    },
    {
        "icc": "89454284200010500094",
        "year": 2019,
        "month": 5,
        "usageDate": "2019-05-13T09:14:35+00:00",
        "bytesIn": 98457,
        "bytesOut": 5894,
        "sessionId": "5a095ef3-pgw-c/64e1a109",
        "imei": "3573100500176526",
        "countryCode": "DK"
    }
]
```

!!! tip
    Keep in mind that the response is given as a list of usages and not returned as a regular top level JSON object.


## Message usage for a sim card

## SMPP usage for a sim card

## Call usage for a sim card

