# SMS forwarding

Deliver SMS from MAP to HTTP/HTTPS.

!!! warning
    This webhook requires special setup, please contact **support@wavely.io**
    
## Payload

Field        | Type          | Description
------------ | ------------- | ------------
fromMsisdn | String | E164 MSISDN, e.g. *+4593709603*
toMsisdn | String | E164 MSISDN, e.g. *+4593709603*
messageText | String |

**Example**

```json
{
	"fromMsisdn": "+4593709603",
	"toMsisdn": "+4523964803",
	"messageText": "Hello. This is a message."
}
```