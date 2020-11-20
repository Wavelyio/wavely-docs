# Message CDR

This webhook details the call usage of sim card, i.e. between who and for how long the call lasted.

## Payload

Field        | Type          | Description
------------ | ------------- | ------------
duration | Number | The call duration, in seconds
caller | String | E164 MSISDN, e.g. *+4593709603*
called | String | E164 MSISDN, e.g. *+4593709603*
fromNetwork | [Network](/general-information/data-types/#network) | The mobile-originating network
toNetwork | [Network](/general-information/data-types/#network) | The mobile-terminating network
usageDate | ISO 8601 DateTime |

**Example**

```json
{
    "duration": 60,
    "caller": "+4593709603",
    "called": "+4593709604",
    "fromNetwork": {
        "country": "DK",
        "tadig": "DNKHU",
        "plmn": "23806"
    },
    "toNetwork": {
        "country": "DK",
        "tadig": "DNKHU",
        "plmn": "23806"
    },
    "usageDate": "2020-11-05T13:42:41.454633"
}
```