# SMS
Using this API, you are able to send SMS directly through our SMSC.

We support both numeric and alphanumeric senders. Some basic rules apply:

* For numeric senders: You must own the MSISDN (telephone number) specified.
* For alphanumeric senders: Maximum 11 characters. Your request will also be checked against a blacklist of senders.
* At this time, only sending to DK phone numbers is supported.

## Endpoint: Send SMS

**Description**

Sends an SMS to the specified receiver, from the specified sender.

**Endpoint**

```
POST /sms
```

**Request Payload**

| Field     | Type   | Description                                                                |
|-----------|--------|----------------------------------------------------------------------------|
| sendTo    | String | E164 MSISDN, e.g. *+4593709603*                                            |
| sendFrom  | String | An alphanumeric sender e.g. 'Wavely' or an E164 MSISDN, e.g. *+4593709603* |
| plainText | String | The SMS itself                                                             |

**Example**

```
{
	"sendTo": "+4523960001",
	"sendFrom": "Wavely",
	"plainText": "Hello! This is an important message from Wavely!"
}
```

**Response Payload**

| Field             | Type    | Description                        |
|-------------------|---------|------------------------------------|
| operatorMessageId | String  | The generated unique ID of the SMS |
| smsCount          | Integer | How many SMS were sent             |

!!! tip
    The `smsCount` is determined by the number of characters sent divided by 160, rounded up.
    This is because the telecommunications network sends that number of SMS behind-the-scenes.

**Error Responses**

| HTTP Status Code | Reason(s)                                           |
|------------------|-----------------------------------------------------|
| 403              | You are using a sender you are not permitted to use |
