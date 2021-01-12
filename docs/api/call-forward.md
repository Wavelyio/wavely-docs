# Callforwarding
This is the API for call forwarding management.

* Get all call forward rules
* Get call forward rule by msisdn
* Delete call forward rule by msisdn
* Create call forward rule

## API Objects

### CallForwardingRule
Field           | Type          | Description
------------    | ------------  | ------------
sourceMsiddn    | String        | Source msisdn of the call forward rule
targetMsisdn    | String        | Target msisdn of the call forward rule
createdDate     | LocalDateTime | Date when rule is created

## Endpoint: Get call forwarding rules

**Description**

Get all call forwarding rules

**Endpoint:** `GET /callforwardings`

**Response Payload**

List([CallForwardingRule](/api/call-forward/#callforwardingrule))

## Endpoint: Get callforwarding rule by msisdn

**Description**

Get call forwarding rule by source msisdn.

**Endpoint:** `GET /callforwardings/{msisdn}`

**Path parameter**

Field           | Type          | Description
------------    | ------------  | ------------
msisdn          | String        | Msisdn to lookup

**Response Payload**

[CallForwardingRule](/api/call-forward/#callforwardingrule)

## Endpoint: Delete call forwarding rule by msisdn

**Description**

Delete call forwarding rule by source msisdn.

**Endpoint:** `DELETE /callforwardings/{msisdn}`

## Endpoint: Create new call forwarding rule

**Description**

Create new call forwarding rule.

**Endpoint:** `POST /callforwardings`

**Request Payload**

Field           | Type          | Description
------------    | ------------  | ------------
sourceMsisdn    | String        | The msisdn to be forwarded
targetMsisdn    | String        | The msisdn to receive the forward
