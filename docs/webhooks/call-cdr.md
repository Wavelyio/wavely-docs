# Message CDR

This webhook details the call usage of sim card, i.e. between who and for how long the call lasted.

## Payload

Field        | Type          | Description
------------ | ------------- | ------------
duration | Number | The call duration, in seconds
caller | String | E164 MSISDN, e.g. *+4593709603*
called | String | E164 MSISDN, e.g. *+4593709603*
fromCountryCode | String | Any alpha-2 country code
toCountryCode | String | Any alpha-2 country code
usageDate | ISO 8601 DateTime |

**Example**

```json
{
	"duration": 60,
	"caller": "+4523964803",
	"called": "+4593709603",
	"fromCountryCode": "DK",
	"toCountryCode": "DK",
	"usageDate": "2019-05-10T12:46:32"
}
```