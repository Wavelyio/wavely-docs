# About
Using this API, you are able to send SMS directly through our SMSC.

We support both numeric and alphanumeric senders. Some basic rules apply:

* For numeric senders: You must own the MSISDN (telephone number) specified.
* For alphanumeric senders: Maximum 11 characters. Your request will also be checked against a blacklist to combat simple fraud attempts.

# API
Below you will find a collection of endpoints for this API.

## Send SMS

**Description**

Sends an SMS to the specified receiver, from the specified sender.

**Endpoint:** `POST /sms`

### Request Payload

Field        | Type          | Description
------------ | ------------- | ------------
sendTo | String | The destination to send to
sendFrom | String | The sender
plainText | String | The SMS itself

**Example**

TODO

### Response Payload

Field        | Type          | Description
------------ | ------------- | ------------
operatorMessageId | String | The generated unique ID of the SMS
smsCount | Integer | How many SMS were sent

!!! tip
    The `smsCount` is determined by the number of characters sent divided by 160, rounded up.
    This is because the telecommunications network sends that number of SMS behind-the-scenes.

!!! bug
    The `smsCount` variable always returns -1 — We are working on improving this.
