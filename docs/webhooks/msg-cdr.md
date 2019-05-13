# Message CDR

This webhook details the SMS usage of SIM card, such as who sent the SMS and who received it, including alphanumeric senders.

## Payload

Field        | Type          | Description
------------ | ------------- | ------------
caller | String | E164 MSISDN, or alphanumeric sender, e.g. *Wavely*
called | String | E164 MSISDN, e.g. *+4523964804*
fromCountryCode | String | Any alpha-2 country code
toCountryCode | String | Any alpha-2 country code
usageDate | ISO 8601 DateTime |

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