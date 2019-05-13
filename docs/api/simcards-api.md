# SIM card API
This is the API for SIM card management. We currently expose the following actions:

* Get SIM cards
* Get single SIM card
* Get status of single SIM card
* Perform action on single SIM card

## Endpoint: Get SIM cards

**Description**

Get SIM cards on account, with pagination, and with multiple optional filters.

**Endpoint:** `GET /simcards`

**Request Query Parameters**

Field        		| Type          | Description  | Required
------------------- | ------------- | ------------ | ------------
page 		 		| Integer 		| Page number for pagination | Yes
limit 		 		| Integer 		| Page size | Yes
iccFilter 			| String 		| Filter for ICC | No
msisdnFilter 		| String 		| Filter for MSISDN | No
imsiFilter  		| String 		| Filter for the IMSI | No

**Response Payload**

Field        | Type          | Description
------------ | ------------- | ------------
totalCount | Long | How many SIM cards are available in total  
simcards | List([SimCard](/general-information/data-types/#simcarddto)) | The SIM card collection

## Endpoint: Get single sim card

**Description**

Queries the system for one SIM card, by ICC.

**Endpoint:** `GET /simcard/{icc}`

**Response Payload**

Field        | Type          | Description
------------ | ------------- | ------------
icc | String | The ICC of the SIM card
msisdn | String | E164 MSISDN, e.g. *+4593709603*
state | [ImsiStates](/general-information/data-types/#imsistates) | The current state of the SIM card
operatorName | String | The name of the underlying telco operator
pin1 | String |
pin2 | String |
puk1 | String |
puk2 | String |

## Endpoint: Get status of single SIM card

**Description**

Provides some additional details about a single SIM card.

**Endpoint:** `GET /simcard/{icc}/status`

**Response Payload**

Field        | Type          | Description
------------ | ------------- | ------------
icc 		| String | The ICC of the SIM card
msisdn 		| String | E164 MSISDN, e.g. *+4593709603*
state 		| [ImsiStates](/general-information/data-types/#imsistates) | The current state of the SIM card
pendingState | [ImsiStates](/general-information/data-types/#imsistates) | The state the SIM card is about to change to
operatorProfileName | String | Name of the operator profile assigned to the SIM card
dataSessionState | [DataSessionStates](/general-information/data-types/#datasessionstates) | Information on the current data state of the SIM card

## Endpoint: Apply action to sim card

**Description**

Apply an action to the specified SIM card, for example "activate SIM card" or "suspend SIM card".

**Endpoint:** `POST /simcard/{icc}/action`

**Request Payload**

Field        | Type          | Description
------------ | ------------- | ------------
action | [SimCardActions](/general-information/data-types/#simcardactions) | The action to apply to the SIM card

**Example**

```
{
	"action": "ACTIVATE"
}
```
