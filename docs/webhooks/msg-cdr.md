# Message CDR

This webhook details the SMS usage of SIM card, such as who sent the SMS and who received it, including alphanumeric senders.

## Payload

Field        | Type          | Description
------------ | ------------- | ------------
caller | String | E164 MSISDN, or alphanumeric sender, e.g. *Wavely*
called | String | E164 MSISDN, e.g. *+4593709603*
fromNetwork | [Network](/general-information/data-types/#network) | The mobile-originating network
toNetwork | [Network](/general-information/data-types/#network) | The mobile-terminating network
usageDate | ISO 8601 DateTime |

**Example**

```json
{
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