# Message CDR

This webhook details the sms usage of sim card, such as who sent the sms and who received it, inclusive alphanumeric senders.

## Payload

Field        | Type          | Description
------------ | ------------- | ------------
caller | String | E164 MSISDN, or alphanumeric sender, e.g. *Wavely*
called | String | E164 MSISDN, e.g. *+4523964804*
fromCountryCode | String | Any alpha-2 country code
toCountryCode | String | Any alpha-2 country code
usageDate | ISO 8601 |

**Example**

```json
{
	"caller": "Wavely",
	"called": "+4523964804",
	"fromCountryCode": "DK",
	"toCountryCode": "DK",
	"usageDate": "2019-05-10T12:46:32"
}
```