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

**Response structure and types**

| Field       | Type              | Description                                                   |
| ----------- | ----------------- | ------------------------------------------------------------- |
| icc         | String            | The unique identifier for the sim card generating the usage.  |
| year        | Number            | Year is given in the ISO format for example 2019.             |
| month       | Number            | Month is represented as a number for example 'april = 4'      |
| usageDate   | ISO 8601 DateTime | In UTC time.                                                  |
| bytesIn     | Number            |                                                               |
| bytesOut    | Number            |                                                               |
| sessionId   | String            | Unique identifier for the session on the network.             |
| imei        | String            | The observed Imei number for the device generating the usage. |
| countryCode | String            | Alpha2 code                                                   |

**Example response**
```json
[
    {
        "icc": "89454284200010500094",
        "year": 2019,
        "month": 5,
        "usageDate": "2019-05-13T09:09:41",
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
        "usageDate": "2019-05-13T09:14:35",
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
Message usage for a given **month** in a given **year** can be accesed by using the following URL:

`GET /simcards/{icc}/usage/msg/{year}/{month}`

**Response structure and types**

| Field           | Type              | Description                                                     |
| --------------- | ----------------- | --------------------------------------------------------------- |
| icc             | String            | The unique identifier for the sim card generating the usage.    |
| year            | Number            | Year is given in the ISO format for example 2019.               |
| month           | Number            | Month is represented as a number for example 'april = 4'        |
| usageDate       | ISO 8601 DateTime | In UTC time.                                                    |
| caller          | String            | Regular string and not necessarily a valid number.              |
| called          | String            | E164 MSISDN, e.g. *+4523964804*                                 |
| fromCountryCode | String            | Alpha2 code                                                     |
| toCountryCode   | String            | Alpha2 code                                                     |
| direction       | String            | One of the following values can be present INCOMING or OUTGOING |

**Example response**

!!! warning ""
    the example is generated to express as many scenarios as possible, therefore not necessarily a possible occurance for an actual sim card.

```json
[
    {
        "icc": "89454284200010500094",
        "year": 2019,
        "month": 5,
        "usageDate": "2019-05-13T09:09:41",
        "caller": "Wavely",
        "called": "+491745553079",
        "fromCountryCode": "DK",
        "toCountryCode": "DE",
        "direction": "INCOMING"
    },
    {
        "icc": "89454284200010500094",
        "year": 2019,
        "month": 5,
        "usageDate": "2019-05-13T09:14:35",
        "caller": "+491745553079",
        "called": "+4593709603",
        "fromCountryCode": "DE",
        "toCountryCode": "DK",
        "direction": "INCOMING"
    },
    {
        "icc": "89454284200010500094",
        "year": 2019,
        "month": 5,
        "usageDate": "2019-05-13T09:14:35",
        "caller": "+4593706589",
        "called": "+4525559603",
        "fromCountryCode": "DK",
        "toCountryCode": "DK",
        "direction": "OUTGOING"
    }
]
```

!!! tip
    Keep in mind that the response is given as a list of usages and not returned as a regular top level JSON object.

## SMPP usage for a sim card
SMPP usage for a given **month** in a given **year** can be accesed by using the following URL:

`GET /simcards/{icc}/usage/smpp/{year}/{month}`

**Response structure and types**

| Field           | Type              | Description                                                     |
| --------------- | ----------------- | --------------------------------------------------------------- |
| icc             | String            | The unique identifier for the sim card generating the usage.    |
| year            | Number            | Year is given in the ISO format for example 2019.               |
| month           | Number            | Month is represented as a number for example 'april = 4'        |
| usageDate       | ISO 8601 DateTime | In UTC time.                                                    |
| caller          | String            | Regular string and not necessarily a valid number.              |
| called          | String            | Regular string and not necessarily a valid number.              |
| fromCountryCode | String            | Alpha2 code                                                     |
| toCountryCode   | String            | Alpha2 code                                                     |
| direction       | String            | One of the following values can be present INCOMING or OUTGOING |

**Example response**

!!! warning ""
    the example is generated to express as many scenarios as possible, therefore not necessarily a possible occurance for an actual sim card.

```json
[
    {
        "icc": "89454284200010500094",
        "year": 2019,
        "month": 5,
        "usageDate": "2019-05-13T09:09:41",
        "caller": "Wavely",
        "called": "+491745553079",
        "fromCountryCode": "DK",
        "toCountryCode": "DE",
        "direction": "INCOMING"
    },
    {
        "icc": "89454284200010500094",
        "year": 2019,
        "month": 5,
        "usageDate": "2019-05-13T09:14:35",
        "caller": "+491745553079",
        "called": "+4593709603",
        "fromCountryCode": "DE",
        "toCountryCode": "DK",
        "direction": "INCOMING"
    },
    {
        "icc": "89454284200010500094",
        "year": 2019,
        "month": 5,
        "usageDate": "2019-05-13T09:14:35",
        "caller": "+4593706589",
        "called": "+4525559603",
        "fromCountryCode": "DK",
        "toCountryCode": "DK",
        "direction": "OUTGOING"
    }
]
```

!!! tip
    Keep in mind that the response is given as a list of usages and not returned as a regular top level JSON object.


## Call usage for a sim card
Call usage for a given **month** in a given **year** can be accesed by using the following URL:

`GET /simcards/{icc}/usage/call/{year}/{month}`

**Response structure and types**

| Field           | Type              | Description                                                                                                                  |
| --------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| icc             | String            | The unique identifier for the sim card generating the usage.                                                                 |
| year            | Number            | Year is given in the ISO format for example 2019.                                                                            |
| month           | Number            | Month is represented as a number for example 'april = 4'                                                                     |
| usageDate       | ISO 8601 DateTime | In UTC time.                                                                                                                 |
| caller          | String            | E164 MSISDN, e.g. *+4523964804*                                                                                              |
| called          | String            | E164 MSISDN, e.g. *+4523964804*                                                                                              |
| duration        | Number            | Duration of the call measured in seconds, the result disregards network connection time. i.e. Only the billed call duration. |
| fromCountryCode | String            | Alpha2 code                                                                                                                  |
| toCountryCode   | String            | Alpha2 code                                                                                                                  |
| direction       | String            | One of the following values can be present INCOMING or OUTGOING                                                              |

**Example response**

```json
[
    {
        "icc": "89454284200010500094",
        "year": 2019,
        "month": 5,
        "usageDate": "2019-05-13T09:14:35",
        "caller": "+491745553079",
        "called": "+4593709603",
        "duration": 849,
        "fromCountryCode": "DE",
        "toCountryCode": "DK",
        "direction": "INCOMING"
    },
    {
        "icc": "89454284200010500094",
        "year": 2019,
        "month": 5,
        "usageDate": "2019-05-13T12:18:24",
        "caller": "+4593706589",
        "called": "+4525559603",
        "duration": 357,
        "fromCountryCode": "DK",
        "toCountryCode": "DK",
        "direction": "OUTGOING"
    }
]
```

!!! tip
    Keep in mind that the response is given as a list of usages and not returned as a regular top level JSON object.