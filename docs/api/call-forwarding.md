# Call forwarding API
Using the endpoints described in this section, you are able to create, modify, and delete call forwarding rules.

!!! warning
    Call Forwarding is not enabled by default. Please contact Wavely about this.

!!! danger
	The call forwarding api only supports forwarding for Danish controlled phone numbers. (+45)

## API Models ##
### CallForwardingRule ###
| Field             | Type                                                                                  |
| ---------------   | ---------------                                                                       |
| id                | Long                                                                                  |
| sourceMsisdn      | E164 MSISDN, e.g. *+4593709603*                                                       |
| targetMsisdn      | E164 MSISDN, e.g. *+4593709603*                                                       |
| status            | [CallForwardingRuleStatus](/general-information/data-types#callforwardingrulestatus)  |

### CallForwardingRules ###
| Field             	| Type                                          |
| ---------------   	| ---------------                               |
| callForwardingRules   | List([CallForwardingRule](/api/call-forwarding#callforwardingrule))	|

### CreateCallForwardingRule ###
Field        | Type          	| Description
------------ | ------------- 	| ------------
sourceMsisdn | String 			| "From" telephone number
targetMsisdn | String 			| "To" telephone number  

### UpdateCallForwardingRule ###
Field        | Type          	| Description
------------ | ------------- 	| ------------
targetMsisdn | String 			| "To" telephone number  

## Endpoint: Get All Call Forwarding Rules

**Description**

Retrieve status and details for all call forwarding rules.

**Endpoint:** `GET /callforwardingrules`

**Response Payload** [CallForwardingRules](/api/call-forwarding#callforwardingrules)

**Example**
```
{
	"callforwardingRules": [
		{
			"id": 919,
			"sourceMsisdn": "+4542895645",
			"targetMsisdn": "+4542652356",
			"status": "PENDING_CREATE"
		}
	]
}
```
## Endpoint: Get (Single) Call Forwarding Rule

**Description**

Retrieve status and details for single call forwarding rule.

**Endpoint:** `GET /callforwardingrules/{id}`

**Response Payload** [CallForwardingRule](/api/call-forwarding#callforwardingrule)

**Example**
```
{
	"id": 919,
	"sourceMsisdn": "+4542895645",
	"targetMsisdn": "+4542652356",
	"status": "PENDING_CREATE"
}
```

## Endpoint: Create Call Forwarding Rule

**Description**

Create a new call forwarding rule.

**Endpoint:** `POST /callforwardingrules`

**Request Payload** [CreateCallForwardingRule](/api/call-forwarding#createcallforwardingrule)

**Example**

```
{
	"sourceMsisdn": "+4511111111",
	"targetMsisdn": "+4522222222"
}
```

**Response Payload** [CallForwardingRule](/api/call-forwarding#callforwardingrule)
**Example**
```
{
	"id": 919,
	"sourceMsisdn": "+4511111111",
	"targetMsisdn": "+4522222222",
	"status": "PENDING_CREATE"
}
```

## Endpoint: Update Call Forwarding Rule

**Description**

Update a forwarding rule with a new target MSISDN.

**Endpoint:** `PUT /callforwardingrules/{id}`

**Request Payload** [UpdateCallForwardingRule](/api/call-forwarding#updatecallforwardingrule)

**Example**

```
{
	"targetMsisdn": "+4533333333"
}
```

**Response Payload** [CallForwardingRule](/api/call-forwarding#callforwardingrule)
**Example**
```
{
	"id": 919,
	"sourceMsisdn": "+4542895645",
	"targetMsisdn": "+4533333333",
	"status": "PENDING_UPDATE"
}
```

## Endpoint: Delete Call Forwarding Rule

**Description**

Delete a call forwarding rule to revoke the call forwarding.

**Endpoint:** `DELETE /callforwardingrules/{id}`
