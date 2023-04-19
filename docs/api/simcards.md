# SIM cards
This is the API for SIM card management. We currently expose the following actions:

* Get SIM cards
* Get single SIM card
* Get status of single SIM card
* Perform action on single SIM card

## Endpoint: Get SIM cards

**Description**

Get SIM cards on account, with pagination, and with multiple optional filters.
To retrieve the remaining pages simply change the page parameter of the query to the next page.

**Endpoint:** `GET /simcards`

**Request Query Parameters**

| Field        | Type    | Description                | Required |
|--------------|---------|----------------------------|----------|
| page         | Integer | Page number for pagination | No       |
| size         | Integer | Page size                  | No       |
| iccFilter    | String  | Filter for ICC             | No       |
| msisdnFilter | String  | Filter for MSISDN          | No       |
| imsiFilter   | String  | Filter for the IMSI        | No       |

!!! info
	The page query parameters is 0-indexed. Such that the initial query will be `/simcards?page=0`

**Response Payload**

[Page](../../general-information/data-types/#page(type))([SimCard](../../general-information/data-types/#simcard))

## Endpoint: Get single SIM card

**Description**

Queries the system for one SIM card, by ICC.

**Endpoint:** `GET /simcards/{icc}`

**Response Payload**

| Field        | Type                                                               | Description                            |
|--------------|--------------------------------------------------------------------|----------------------------------------|
| icc          | String                                                             | The ICC of the SIM card                |
| msisdn       | String                                                             | E164 MSISDN, e.g. *+4593709603*        |
| state        | [ImsiStates](../../general-information/data-types/#imsistates)     | The current state of the SIM card      |
| pin1         | String                                                             | Primary pin code for the SIM card      |
| pin2         | String                                                             | Secondary pin code for the SIM card    |
| puk1         | String                                                             | Primary puk code for the SIM card      |
| puk2         | String                                                             | Secondary puk code for the SIM card    |
| networkSpeed | [NetworkSpeed](../../general-information/data-types/#networkspeed) | Network speed property of the SIM card |

## Endpoint: Get status of single SIM card

**Description**

Provides some additional details about a single SIM card.

**Endpoint:** `GET /simcards/{icc}/status`

**Response Payload**

| Field               | Type                                                                         | Description                                           |
|---------------------|------------------------------------------------------------------------------|-------------------------------------------------------|
| icc                 | String                                                                       | The ICC of the SIM card                               |
| msisdn              | String                                                                       | E164 MSISDN, e.g. *+4593709603*                       |
| state               | [ImsiStates](../../general-information/data-types/#imsistates)               | The current state of the SIM card                     |
| pendingState        | [ImsiStates](../../general-information/data-types/#imsistates)               | The state the SIM card is about to change to          |
| operatorProfileName | String                                                                       | Name of the operator profile assigned to the SIM card |
| dataSessionState    | [DataSessionStates](../../general-information/data-types/#datasessionstates) | Information on the current data state of the SIM card |

## Endpoint: Apply action to SIM card

**Description**

Apply an action to the specified SIM card, for example "activate SIM card" or "suspend SIM card".

**Endpoint:** `POST /simcards/{icc}/action`

**Request Payload**

| Field         | Type                                                                   | Description                                |
|---------------|------------------------------------------------------------------------|--------------------------------------------|
| simCardAction | [SimCardActions](../../general-information/data-types/#simcardactions) | The action to apply to the SIM card        |
| networkSpeed  | [NetworkSpeed](../../general-information/data-types/#networkspeed)     | The network speed to apply to the SIM card |

**Example**
```json
{
	"simCardAction": "ACTIVATE"
}
```
```json
{
	"simCardAction": "THROTTLE",
	"networkSpeed": "MBIT_1"
}
```
```json
{
	"simCardAction": "ACTIVATE",
	"networkSpeed": "MBIT_5"
}
```
```json
{
	"simCardAction": "SUSPEND"
}
```
```json
{
	"simCardAction": "UNTHROTTLE"
}
```

## Endpoint: Update operator profile for SIM card

**Description**

Update the operator profile for a single SIM card

**Endpoint:** `PUT /simcards/{icc}/operatorprofiles`

**Request Payload**

| Field              | Type  | Description                   |
|--------------------|-------|-------------------------------|
| operatorProfileId  | Long  | The operator profile to apply |

## Endpoint: Remove SIM card from its SIM card group if present

**Description**

Remove the SIM card group relation for the SIM card

**Endpoint:** `DELETE /simcards/{icc}/simcardgroup`
