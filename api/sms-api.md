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

**Payload:**

Field        | Type          | Description
------------ | ------------- | ------------
Content Cell | Content Cell  | Content Cell
Content Cell | Content Cell  | Content Cell
