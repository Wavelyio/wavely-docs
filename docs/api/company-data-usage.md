# Company Data Usage
This is the API for querying company data usage. We currently expose the following actions:

* Get data usage as a total for a company in a month
* Get data usage for a company in a month, grouped by SIM card collections
* Get data usage for a company in a month, for a specified SIM card collections

## Endpoint: Get data usage for company in month

**Description**

Get the data usage of a company in a month, as a total value in bytes.

**Endpoint:** `GET /usage/data/{year}/{month}`

**Request Query Parameters**

| Field | Type    | Description                            | Required |
|-------|---------|----------------------------------------|----------|
| year  | Integer | Year to see data usage in              | Yes      |
| month | String  | Month, in text, to see consumption for | Yes      |

**Response Payload**

[DataUsageByCompany](../../general-information/data-types/#datausagebycompany)

## Endpoint: Get data usage for SIM card collections in month

**Description**

Get the data usage of a company in a month, grouped by SIM card groups.

**Endpoint:** `GET /usage/data/collections/{year}/{month}`

**Response Payload**

| Field | Type    | Description                            | Required |
|-------|---------|----------------------------------------|----------|
| year  | Integer | Year to see data usage in              | Yes      |
| month | String  | Month, in text, to see consumption for | Yes      |

List([DataUsageBySimCardCollections](../../general-information/data-types/#datausagebysimcardcollections))

## Endpoint: Get data usage for SIM card group in month

**Description**

**Endpoint:** `GET /usage/data/collections/{collectionId}/{year}/{month}`

**Response Payload**

| Field        | Type    | Description                                                  | Required |
|--------------|---------|--------------------------------------------------------------|----------|
| collectionId | UUID    | Unique ID for the SIM card collection we want data usage for | Yes      |
| year         | Integer | Year to see data usage in                                    | Yes      |
| month        | String  | Month, in text, to see consumption for                       | Yes      |

[DataUsageBySimCardCollections](../../general-information/data-types/#datausagebysimcardcollections)
