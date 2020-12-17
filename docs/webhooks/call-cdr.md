# Call CDR

This webhook details the call usage of sim card, i.e. between who and for how long the call lasted.

## Payload

Field        | Type          | Description
------------ | ------------- | ------------
duration | Number | The call duration, in seconds
caller | String | E164 MSISDN, e.g. *+4593709603*
called | String | E164 MSISDN, e.g. *+4593709603*
fromNetwork | [Network](/general-information/data-types/#network) | The mobile-originating network
toNetwork | [Network](/general-information/data-types/#network) | The mobile-terminating network
icc | String | The SIM-card identifier
imsi | String | International mobile subscriber identity
usageDate | ISO 8601 DateTime |

**Example**

!!! danger
	As shown in the examples, information on both networks will never be available. 
    Depending on the direction of the call, either the originating network or the destination network will be present.
    In the case of the caller being known the originating network will be present and otherwise the destination network.

```json
{
    "duration": 60,
    "caller": "+4593709603",
    "called": "+4593709604",
    "fromNetwork": null,
    "toNetwork": {
        "country": "DK",
        "tadig": "DNKHU",
        "plmn": "23806"
    },
    "icc": "89454284200010500045",
    "imsi": "238420001050004",
    "usageDate": "2020-11-05T13:42:41.454633"
}
```

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
    "toNetwork": null,
    "icc": "89454284200010500045",
    "imsi": "238420001050004",
    "usageDate": "2020-11-05T13:42:41.454633"
}
```
