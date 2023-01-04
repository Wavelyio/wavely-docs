# SIM card usage

Usage for individual SIM cards can be accessed using the usage API.

We partition usage into four categories:

* Data
* SMS
* SMPP
* Call

Each of these categories have their own endpoint requiring that requests specify the **month** and **year** for which to
retrieve the usage.

Parameters for **years** must be given in the ISO 8601 **year** format, such as 2019.  
Months must be specified using the English names for months, such as `january`, `march`, and `july`.

When querying it is also required to specify which SIM card the usage should be retrieved for.
This is done using the **ICC** identifier of a SIM card.

## Data usage for a SIM card

Data usage for a given **month** in a given **year** can be accessed by using the following URL:

`GET /simcards/{icc}/usage/data/{year}/{month}`

**Response structure and types**

| Field       | Type              | Description                                                   |
|-------------|-------------------|---------------------------------------------------------------|
| icc         | String            | The unique identifier for the SIM card generating the usage.  |
| year        | Number            | Year is given in the ISO 8601 format for example 2019.        |
| month       | Number            | Month is represented as a number for example 'april = 4'      |
| usageDate   | ISO 8601 DateTime | In UTC time.                                                  |
| bytesIn     | Number            |                                                               |
| bytesOut    | Number            |                                                               |
| sessionId   | String            | Unique identifier for the session on the network.             |
| imei        | String            | The observed IMEI number for the device generating the usage. |
| countryCode | String            | Alpha-2 code                                                  |

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

## Message usage for a SIM card

Message usage for a given **month** in a given **year** can be accessed by using the following URL:

`GET /simcards/{icc}/usage/msg/{year}/{month}`

**Response structure and types**

| Field           | Type                                                     | Description                                                       |
|-----------------|----------------------------------------------------------|-------------------------------------------------------------------|
| icc             | String                                                   | The unique identifier for the SIM card generating <br> the usage. |
| year            | Number                                                   | Year is given in the ISO 8601 format for example 2019.            |
| month           | Number                                                   | Month is represented as a number for example 'april = 4'          |
| usageDate       | ISO 8601 DateTime                                        | In UTC time.                                                      |
| caller          | String                                                   | Regular string and not necessarily a valid number.                |
| called          | String                                                   | E164 MSISDN, e.g. *+4593709603*                                   |
| fromCountryCode | String                                                   | Alpha-2 code                                                      |
| toCountryCode   | String                                                   | Alpha-2 code                                                      |
| direction       | [Directions](/general-information/data-types#directions) |                                                                   |

**Example response**

!!! warning ""
The example is generated to express as many scenarios as possible, therefore not necessarily a possible occurrence for
an actual SIM card.

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

## SMPP usage for a SIM card
SMPP usage for a given **month** in a given **year** can be accessed by using the following URL:

`GET /simcards/{icc}/usage/smpp/{year}/{month}`

**Response structure and types**

| Field           | Type                                                     | Description                                                       |
|-----------------|----------------------------------------------------------|-------------------------------------------------------------------|
| icc             | String                                                   | The unique identifier for the SIM card generating <br> the usage. |
| year            | Number                                                   | Year is given in the ISO 8601 format for example 2019.            |
| month           | Number                                                   | Month is represented as a number for example 'april = 4'          |
| usageDate       | ISO 8601 DateTime                                        | In UTC time.                                                      |
| caller          | String                                                   | Regular string and not necessarily a valid number.                |
| called          | String                                                   | Regular string and not necessarily a valid number.                |
| fromCountryCode | String                                                   | Alpha-2 code                                                      |
| toCountryCode   | String                                                   | Alpha-2 code                                                      |
| direction       | [Directions](/general-information/data-types#directions) |                                                                   |

**Example response**

!!! warning ""
    the example is generated to express as many scenarios as possible, therefore not necessarily a possible occurrence for an actual SIM card.

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

## Call usage for a SIM card

Call usage for a given **month** in a given **year** can be accessed by using the following URL:

`GET /simcards/{icc}/usage/call/{year}/{month}`

**Response structure and types**

| Field           | Type                                                     | Description                                                                                                                            |
|-----------------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| icc             | String                                                   | The unique identifier for the SIM card generating <br> the usage.                                                                      |
| year            | Number                                                   | Year is given in the ISO 8601 format for example 2019.                                                                                 |
| month           | Number                                                   | Month is represented as a number for example 'april = 4'                                                                               |
| usageDate       | ISO 8601 DateTime                                        | In UTC time.                                                                                                                           |
| caller          | String                                                   | E164 MSISDN, e.g. *+4593709603*                                                                                                        |
| called          | String                                                   | E164 MSISDN, e.g. *+4593709603*                                                                                                        |
| duration        | Number                                                   | Duration of the call measured in seconds, the result <br> disregards network connection time. i.e. Only the billed <br> call duration. |
| fromCountryCode | String                                                   | Alpha-2 code                                                                                                                           |
| toCountryCode   | String                                                   | Alpha-2 code                                                                                                                           |
| direction       | [Directions](/general-information/data-types#directions) |                                                                                                                                        |

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

## Total usage for a SIM card

Get the total data usage of a specific SIM card for a given **period** can be accessed by using the following URL:

`POST /simcardexternalapi/simcardusage`

**Request body structure and types**

Request body contains GetSimCardUsageDTO with such fields:

| Field         | Type         | Description                                              |
|---------------|--------------|----------------------------------------------------------|
| iccs          | List<String> | The list of unique identifiers of the SIM cards          |
| startDateTime | String       | Start date and time of period for getting SIM card usage |
| endDateTime   | String       | End date and time of period for getting SIM card usage   |

**Example request body**

```json
  {
    "iccs" : ["89454284200010507412", "89454284200010507420"],
    "startDateTime" : "2021-02-01T00:00:01.715",
    "endDateTime" : "2021-08-01T00:00:01.715"
  }
```

**Response structure and types**

| Field         | Type   | Description                                                 |
|---------------|--------|-------------------------------------------------------------|
| icc           | String | The unique identifier for the SIM card generating the usage |
| sumTotalBytes | Long   | The total data usage sum of bytes of SIM card               |

**Example response**

```json
[
  {
    "icc": "89454284200010507412",
    "sumTotalBytes": 334143637
  },
  {
    "icc": "89454284200010507420",
    "sumTotalBytes": 300093575
  }
]
```