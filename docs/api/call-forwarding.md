# Call Forwarding API
Using the endpoints described in this section, you are able to create, modify, and delete call forwarding rules.

!!! warning
    Call Forwarding is not enabled by default. Please contact Wavely about this.

## Endpoint: Get All Call Forwarding Rule

**Description**

Retrieve status and details for all call forwarding rules.

**Endpoint:** `GET /callforwardingrules`

## Endpoint: Get (Single) Call Forwarding Rule

**Description**

Retrieve status and details for single call forwarding rule.

**Endpoint:** `GET /callforwardingrules/{id}`

## Endpoint: Create Call Forwarding Rule

**Description**

Create a new call forwarding rule.

**Endpoint:** `POST /callforwardingrules`

<h3>Request Payload</h3>

Field        | Type          | Description
------------ | ------------- | ------------
sourceMsisdn | String | "From" telephone number
targetMsisdn | String | "To" telephone number  

**Example**

```
{
	"sourceMsisdn": "4511111111",
	"targetMsisdn": "4522222222"
}
```

## Endpoint: Update Call Forwarding Rule

**Description**

Update a forwarding rule with a new target MSISDN.

**Endpoint:** `PUT /callforwardingrules/{id}`

<h3>Request Payload</h3>

Field        | Type          | Description
------------ | ------------- | ------------
targetMsisdn | String | The new "to" telephone number  

**Example**

```
{
	"targetMsisdn": "4533333333"
}
```

## Endpoint: Delete Call Forwarding Rule

**Description**

Delete a call forwarding rule to revoke the HLR forwarding.

**Endpoint:** `DELETE /callforwardingrules/{id}`
