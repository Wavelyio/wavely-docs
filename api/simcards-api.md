# About
This is the API for sim card management. We currently expose the following actions:

* Get sim cards
* Get single sim card
* Get status of single sim card
* Perform action on single sim card

# Endpoint: Get sim cards

**Description**

Get sim cards on account, with pagination, and with multiple optional filters.

**Endpoint:** `GET /simcards`

<h3>Request Query Parameters</h3>

Field        | Type          | Description  | Required
------------ | ------------- | ------------ | ------------
page | Integer | Page number for pagination | Yes
limit | Integer | Page size | Yes
iccFilter | String | Filter for ICC | No
msisdnFilter | String | Filter for MSISDN | No
operatorNameFilter  | String | Filter for operator name | No

<h3>Response Payload</h3>

Field        | Type          | Description
------------ | ------------- | ------------
totalCount | Long | How many sim cards are available in total  
simcards | List([SimCard](/user-guide/data-types/#simcarddto)) | The sim card collection

# Endpoint: Get status of single sim card

**Description**

Provides some additional details about a single sim card.

**Endpoint:** `GET /simcard/{icc}/status`

<h3>Response Payload</h3>

Field        | Type          | Description
------------ | ------------- | ------------
icc | String | The ICC of the sim card
msisdn | String | The phone number of the sim, if it has any
state | [SimCardState](/user-guide/data-types/#simcardstate) | The current state of the sim card
