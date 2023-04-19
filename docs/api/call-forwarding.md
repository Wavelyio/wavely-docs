# Call Forwarding
This is the API for call forwarding management.

* Get all call forward rules
* Get call forward rule by msisdn
* Delete call forward rule by msisdn
* Create call forward rule

## API Objects

### CallForwardingRule
| Field             | Type                  | Description                                     |
|-------------------|-----------------------|-------------------------------------------------|
| sourceMsisdn      | String                | Source msisdn of the call forward rule          |
| targetMsisdn      | String                | Target msisdn of the call forward rule          |
| anonymousCallerId | Boolean               | Enable anonymous caller id when forwarding call |
| createdDate       | ISO 8601 DateTime UTC | Date when rule is created                       |

## Endpoint: Get call forwarding rules

**Description**

Get all call forwarding rules

**Endpoint:** `GET /callforwardings`

**Response Payload**

List([CallForwardingRule](../call-forwarding/#callforwardingrule))

**Example response**

```
[
  {
    "sourceMsisdn": "+4522222222",
    "targetMsisdn": "+4533333333",
    "anonymousCallerId": false,
    "createdDate": "2021-01-01T22:33:44"
  },
  {
    "sourceMsisdn": "+4544445566",
    "targetMsisdn": "+4599887766",
    "anonymousCallerId": true,
    "createdDate": "2020-12-12T11:22:33"
  }
]
```

## Endpoint: Get call forwarding rule by msisdn

**Description**

Get call forwarding rule by source msisdn.

**Endpoint:** `GET /callforwardings/{msisdn}`

**Path parameter**

| Field  | Type   | Description      |
|--------|--------|------------------|
| msisdn | String | Msisdn to lookup |

**Response Payload**

[CallForwardingRule](../call-forwarding/#callforwardingrule)

**Example response**

```
{
  "sourceMsisdn": "+4577889900",
  "targetMsisdn": "+4588990001",
  "anonymousCallerId": false,
  "createdDate": "2020-12-12T22:33:44"
}
```

## Endpoint: Delete call forwarding rule by msisdn

**Description**

Delete call forwarding rule by source msisdn.

**Endpoint:** `DELETE /callforwardings/{msisdn}`

## Endpoint: Create new call forwarding rule

**Description**

Create new call forwarding rule.

**Endpoint:** `POST /callforwardings`

**Request Payload**

| Field             | Type    | Description                                   |
|-------------------|---------|-----------------------------------------------|
| sourceMsisdn      | String  | The msisdn to be forwarded                    |
| targetMsisdn      | String  | The msisdn to receive the forward             |
| anonymousCallerId | Boolean | If caller id should be hidden on callee phone |

**Example**

```
{
    "sourceMsisdn": "+4522222222",
    "targetMsisdn": "+4544444444",
    "anonymousCallerId": true
}
```
