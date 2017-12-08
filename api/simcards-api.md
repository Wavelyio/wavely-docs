# About
This is the API for sim card management. We currently expose the following actions:

* Get sim cards
* Get single sim card
* Get status of single sim card
* Perform action on single sim card

# Endpoint: Get sim cards

**Description**

Get sim cards on account, with pagination, and with multiple optional filters.

**Endpoint**

```
GET /simcards
```

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
operatorMessageId | String | The generated unique ID of the SMS
smsCount | Integer | How many SMS were sent

!!! tip
    The `smsCount` is determined by the number of characters sent divided by 160, rounded up.
    This is because the telecommunications network sends that number of SMS behind-the-scenes.

<h3>Error Responses</h3>

HTTP Status Code        | Reason(s)        |
----------------------- | ---------------- |
401 | Invalid API key.
403 | You are using a sender you are not permitted to use.
500 | The server encountered an unhandled error!
