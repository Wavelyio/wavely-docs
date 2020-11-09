# Data CDR

This webhook details the data usage of SIM card, such as how much data was uploaded, downloaded, from which device, and in which country.

Data usage is incremental; it will detail how much data was transmitted since the previous recording. 

## Payload

Field        | Type          | Description
------------ | ------------- | ------------
bytesIn | Number |
bytesOut | Number |
network | [Network](/general-information/data-types/#network) | The mobile network used
sessionId | String | The mobile network data session ID
imei | String | The IMEI number of the device using data
usageDate | ISO 8601 DateTime |
icc | String | The SIM card identifier

**Example**

```json
{
    "bytesIn": 1234,
    "bytesOut": 4321,
    "network": {
        "country": "DK",
        "tadig": "DNKHU",
        "plmn": "23806"
    },
    "sessionId": "5b2244da-pgw-c/6faf764",
    "imei": "9900120101772509",
    "usageDate": "2020-11-05T13:38:48.045093",
    "icc": "89454211095593135450"
}
```