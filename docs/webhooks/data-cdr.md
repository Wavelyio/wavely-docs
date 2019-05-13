# Data CDR

This webhook details the data usage of sim card, such as how much data was uploaded, downloaded, from which device, and in which country.

Data usage is incremental; it will detail how much data was transmitted since the previous recording. 

## Payload

Field        | Type          | Description
------------ | ------------- | ------------
bytesIn | Number |
bytesOut | Number |
countryCode | String | Any alpha-2 country code
sessionId | String | The mobile network data session ID
imei | String | The IMEI number of the device using data
usageDate | ISO 8601 |
icc | String | The sim card identifier

**Example**

```json
{
	"bytesIn": 4321,
	"bytesOut": 1234,
	"countryCode": "DK",
	"sessionId": "5b2244da-pgw-c/6faf764",
	"imei": "9900120101772509",
	"usageDate": "2019-05-10T12:46:32",
	"icc": "89454284200010500060"
}
```