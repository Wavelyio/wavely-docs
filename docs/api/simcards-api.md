# SimCards API
This is the API for sim card management. We currently expose the following actions:

* Get sim cards
* Get single sim card
* Get status of single sim card
* Perform action on single sim card

## Endpoint: Get sim cards

**Description**

Get sim cards on account, with pagination, and with multiple optional filters.

**Endpoint:** `GET /simcards`

**Request Query Parameters**

Field        | Type          | Description  | Required
------------ | ------------- | ------------ | ------------
page | Integer | Page number for pagination | Yes
limit | Integer | Page size | Yes
iccFilter | String | Filter for ICC | No
msisdnFilter | String | Filter for MSISDN | No
operatorNameFilter  | String | Filter for operator name | No

**Response Payload**

Field        | Type          | Description
------------ | ------------- | ------------
totalCount | Long | How many sim cards are available in total  
simcards | List([SimCard](/docs/user-guide/data-types/#simcarddto)) | The sim card collection

## Endpoint: Get single sim card

**Description**

Queries the system for one sim card, by ICC.

**Endpoint:** `GET /simcard/{icc}`

**Response Payload**

Field        | Type          | Description
------------ | ------------- | ------------
icc | String | The ICC of the sim card
msisdn | String | The phone number of the sim, if it has any
state | [SimCardState](/docs/user-guide/data-types/#simcardstate) | The current state of the sim card
operatorName | String | The name of the underlying telco operator
pin1 | String |
pin2 | String |
puk1 | String |
puk2 | String |

## Endpoint: Get status of single sim card

**Description**

Provides some additional details about a single sim card.

**Endpoint:** `GET /simcard/{icc}/status`

<h3>Response Payload</h3>

Field        | Type          | Description
------------ | ------------- | ------------
icc | String | The ICC of the sim card
msisdn | String | The phone number of the sim, if it has any
state | [SimCardState](/docs/user-guide/data-types/#simcardstate) | The current state of the sim card

## Endpoint: Apply action to sim card

**Description**

Apply an action to the specified sim card, for example "activate sim card" or "suspend sim card".

**Endpoint:** `POST /simcard/{icc}/action`

**Request Payload**

Field        | Type          | Description
------------ | ------------- | ------------
action | [SimCardActions](/docs/user-guide/data-types/#simcardactions) | The action to apply to the sim card

**Example**

```
{
	"action": "ACTIVATE"
}
```

**Response Payload**

Field        | Type          | Description
------------ | ------------- | ------------
icc | String | The ICC of the sim card
msisdn | String | The phone number of the sim, if it has any
state | [SimCardState](/docs/user-guide/data-types/#simcardstate) | The current state of the sim card
